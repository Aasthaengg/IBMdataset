N=int(input())
A=list(map(int,input().split()))

X=0
for a in A:
    X+=1/a
print(1/X)