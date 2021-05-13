a,b=map(int,input().split())

ans1=a+b
ans2=a-b
ans3=a*b
ans=[ans1,ans2,ans3]
print(max(ans))