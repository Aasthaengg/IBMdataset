n=int(input())
a,b=map(int,input().split())
p=list(map(int,input().split()))
q1,q2=0,0
for i in range(n):
    if p[i]<=a:
        q1+=1
    elif p[i]<=b:
        q2+=1
print(min(q1,q2,n-(q1+q2)))