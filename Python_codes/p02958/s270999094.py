n = int(input())
A=[int(i)-1 for i in input().split()]
res = 0
for i in range(n):
    if A[i]==i:
        continue
    else:
        res+=1
if(res < 3):print("YES")
else:print("NO")
