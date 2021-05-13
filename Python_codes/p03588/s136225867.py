N = int(input())
ABs = []
for _ in range(N):
    A,B = list(map(int, input().split()))
    ABs.append([A,B])

ABs.sort(key=lambda x: x[0])
ans = 0

A,B = ABs[0]
ans += A-1

for i in range(1,N):
    A,B = ABs[i]
    A_prev,B_prev = ABs[i-1]

    ans += A - A_prev - 1

ans += ABs[-1][1]
ans += N

print(ans)