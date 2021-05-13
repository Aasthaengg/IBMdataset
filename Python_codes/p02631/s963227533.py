n=int(input())
lst=list(map(int,input().split()))
p=0
for i in range(n):
    p=(p^lst[i]) #全体のxor

ans=[]

for i in range(n):
    q=(p^lst[i]) #自分の数値
    ans.append(str(q))
    
print(" ".join(ans))