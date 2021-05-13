n=int(input())
l=[]
for i in range(n):
    r=list(map(int,input().split()))
    l.append(r)
s=0
for i in l:
    s+=i[-1]-i[0]+1
print(s)