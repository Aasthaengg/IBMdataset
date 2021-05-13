n=int(input())
s=list(map(int,input().split()))
k=int(input())
l=[]
for i in range(k):
    p,x=map(int,input().split())
    l.append(sum(s)-s[p-1]+x)
    
for i in range(k):
    print(l[i])