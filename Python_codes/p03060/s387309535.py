N = int(input())
Value = list(map(int, input().split()))
Cost = list(map(int, input().split()))
ans = 0
for i in range(N):
    Happy = Value[i]-Cost[i]
    if Happy > 0:
        ans += Happy
print(ans)
