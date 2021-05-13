N = int(input())
A = list(map(int, input().split()))

# N が 2 で何回割れるか
def how_many_times(N):
    exp = 0
    while N % 2 == 0:
        N //= 2
        exp += 1
    return exp

result = min([how_many_times(v) for v in A])
print(result)