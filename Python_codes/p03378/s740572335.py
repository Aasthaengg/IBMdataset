n,m,x=map(int,input().split())
a=list(map(int,input().split()))
ans_1=0
ans_2=0
for i in range(x):
    if i in a:
        ans_1+=1
for i in range(x,n):
    if i in a:
        ans_2+=1
print(min(ans_1,ans_2))