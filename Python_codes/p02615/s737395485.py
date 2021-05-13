import math

N = int(input())
friendliness = list(map(int, input().split()))
friendliness.sort(reverse=True)

ans = friendliness[0]

for i in range(1, N - 1):
    idx = math.ceil(i/2)
    ans += friendliness[idx]

print(ans)
