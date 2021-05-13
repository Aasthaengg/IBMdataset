n=int(input())
d=[int(input())for i in range(n)]
num=[0 for i in range(max(d)+1)]
for i in d:
    num[i]+=1
ans=len(num)-num.count(0)
print(ans)