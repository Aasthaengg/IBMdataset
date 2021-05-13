from math import gcd

N, M = [int(x) for x in input().split()]
S = input()
T = input()

lcm = N * M // gcd(N, M)
count = 1

result = -1


def check(answer_length, line, answer):
    for i in range(0, len(line)):
        idx = i * answer_length // len(line) + 1

        if idx in answer:
            if not answer[idx] == line[i]:
                return False
        else:
            if idx <= answer_length:
                answer[idx] = line[i]
            else:
                return False

    return True


answer = {}
max_str = max((M-1) * (lcm * count) // M + 1,
                  (N-1) * (lcm * count) // N + 1)

if check(lcm * count, S, answer):
    if check(lcm*count, T, answer):
        print(lcm*count)
        exit()

print(result)
