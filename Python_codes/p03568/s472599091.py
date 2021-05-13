N=int(input())
A=list(map(int,input().split()))

T=0
for a in A:
    T+=(a%2==0)
    
print(3**N-2**T)
