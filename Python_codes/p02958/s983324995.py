N = int(input())
count = 0
Nlist = list(map(int, input().split()))
for i in range(1, N+1):
    count += Nlist[i-1] == i
if count+2 >= N:
    ans = "YES"
else:
    ans = "NO"
print(ans)
