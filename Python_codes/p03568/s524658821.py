N=int(input())
A=list(map(int,input().split()))
evens=0
for a in A:
    if a%2==0:
        evens+=1

ans=3**N-2**evens
print(ans)