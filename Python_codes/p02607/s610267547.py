n = int(input())
arr = list(map(int,input().split()))
ans = 0
for i in range(0,len(arr)+(n%2),2):
    if arr[i] % 2 != 0:
        ans += 1
print(ans)