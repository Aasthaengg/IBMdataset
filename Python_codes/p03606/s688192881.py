n=int(input())
l=[]
for i in range(n):
    s,t=map(int,input().split())
    l.append(t-s+1)
print(sum(l))