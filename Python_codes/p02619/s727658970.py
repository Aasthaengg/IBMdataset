
import sys
input = sys.stdin.readline
d=int(input())
c=list(map(int,input().split()))
s=[]
for _ in range(d):
    s.append(list(map(int,input().split())))
t=[]
for _ in range(d):
    t.append(int(input()))

ld=[-1]*26
sc=0
for i in range(d):
    sc+=s[i][t[i]-1]
    ld[t[i]-1]=i

    C=0
    for j in range(26):
        C+=c[j]*(i-ld[j])
    sc-=C
    print(sc)