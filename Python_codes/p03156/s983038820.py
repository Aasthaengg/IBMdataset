N=int(input())
A,B=map(int,input().split())
p = list(map(int,input().split()))
c=[]
d=[]
e=[]
for i in range(N):
    if p[i]<=A:
        c.append(p[i])
    if A+1 <= p[i] <= B:
        d.append(p[i])
    if B+1 <= p[i]:
        e.append(p[i])

        
print(min(len(c),len(d),len(e)))