n=int(input())
s=input()
a,b=0,0 # a:'.'の個数 b:'#'の個数
x=0 # x:'.'の個数
for i in s:
    if i==".":
        x+=1
ans=x
for i in s:
    if i==".":
        a+=1
    else:
        b+=1
    ans=min(ans,b+x-a)
print(ans)