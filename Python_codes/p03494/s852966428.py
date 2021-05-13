N=int(input())
an=list(map(int,input().split()))
n=0
while(all(a%2==0 for a in an)):
    an=[a//2 for a in an]
    n+=1
print(n)