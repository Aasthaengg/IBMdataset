n=int(input())
a,b=map(int,input().split())
p=list(map(int,input().split()))
q=[0,0,0]
for x in p:
    if x<=a: q[0]+=1
    elif x>a and x<=b: q[1]+=1
    else: q[2]+=1

print(min(q))