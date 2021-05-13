from collections import *
def gcd(a,b):
    if a%b==0:return(b)
    else:return(gcd(b,a%b))

def soinsuu(n):
    visited=defaultdict(int)
    for i in range(2,round(n**.5)+1):
        while n%i==0:
            n//=i
            visited[i]+=1
    if n>1:
        visited[n]+=1
    return(visited)

N=int(input())
A=list(map(int,input().split()))
visited=set()
flg=False
for a in A:
    for i in soinsuu(a):
        if i in visited:
            flg=True
            break
        else:
            visited.add(i)

    if flg:
        break
else:
    print("pairwise coprime")
    exit()

n=A[0]
for a in A[1:]:
    n=gcd(n,a)



if n>1:
    print("not coprime")
else:
    print("setwise coprime")
