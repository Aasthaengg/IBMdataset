def readInt():
    return list(map(int,input().split()))
n = int(input())
l = []
for i in range(1,n):
    ans = 0
    j = i
    k = n-i
    while j>0:
        ans += int(j%10)
        j = int(j/10)
    while k>0:
        ans += int(k%10)
        k = int(k/10)
    l.append(ans)
# print(l)
print(min(l))