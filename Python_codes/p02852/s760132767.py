import sys
N, M = map(int, input().split())
S = input()
S = list(reversed(S))

position = 0
count = 0
answer = []
while True:
    for i in range(M, -1, -1):
        if i == 0:
            print(-1)
            sys.exit()
        if position + i > N:
            continue
        if S[position + i] == '0':
            answer.append(i)
            position += i
            break
    if position >= N:
        break
for i in reversed(answer):
    print(i)
