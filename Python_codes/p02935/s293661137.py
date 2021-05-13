N = int(input())
v = list(map(int, input().split()))

V = sorted(v)

ans = V[0]

for i in range(N-1):
    ans = (ans + V[i+1]) /2

print(ans)

