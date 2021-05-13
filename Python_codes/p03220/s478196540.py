n=int(input())
t,a=map(int,input().split())
H=list(map(int,input().split()))
ans=[]
for h in H:
    ans.append(abs(a-(t-h*0.006)))
print(ans.index(min(ans))+1)