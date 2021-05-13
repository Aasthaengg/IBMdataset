import sys
def input():
    return sys.stdin.readline()[:-1]
N,K=map(int, input().split())
s=[None]*N
for i in range(N):
    t,d=map(int,input().split())
    s[i]=(d,t)
s.sort(reverse=True)
l=[0]*N
d=0
for i in s[:K]:
    l[i[1]-1]+=1
    d+=i[0]
c=0
for i in l:
    if i:
        c+=1
a=d+c**2
h=K-1
for i in s[K:]:
    if not l[i[1]-1]:
        while h>=0:
            if l[s[h][1]-1]>1:
                l[i[1]-1]=1
                l[s[h][1]-1]-=1
                c+=1
                d=d+i[0]-s[h][0]
                a=max(a,d+c**2)
                h-=1
                break
            h-=1
        else:
            break
print(a)