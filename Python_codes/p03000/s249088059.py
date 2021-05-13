N, X = map(int, input().split())
arr = list(map(int, input().split()))

ans =1
height=0
for i in range(N):
    height += arr[i]
    if height > X:
        break
    ans += 1

print(ans)
