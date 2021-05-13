n=int(input())
abc=[]
for _ in range(n):
    a,b=map(int,input().split())
    c=a+b
    abc.append((a,b,c))
abc=sorted(abc,key=lambda x:x[2],reverse=True)
t=abc[::2]
a=abc[1::2]
ans=0
for i in t:
    ans+=i[0]
for i in a:
    ans-=i[1]
print(ans)