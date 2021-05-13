n = int(input())
arr = list(map(int,input().split()))

ans = 1
out = 1
for i in range(n):
    if arr[i]%2 == 0:
        ans *= 3
        out *= 2
    else:
        ans *= 3
        out *= 1

print(ans-out)