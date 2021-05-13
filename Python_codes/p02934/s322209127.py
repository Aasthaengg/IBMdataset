N=int(input())
list=list(map(float, input().split()))
c=0
for i in list:
    list[c]=1/(list[c])
    c+=1
ans=1/(sum(list))
print(ans)
