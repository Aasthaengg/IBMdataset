n=int(input())
s=input()
list1=[0]*(n+1)
ans=0
for i in range(n):
    if s[i]=='I':
        ans+=1
    else:
        ans-=1
    list1[i]=ans
print(max(list1))