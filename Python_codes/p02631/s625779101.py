N=int(input())
a=list(map(int,input().split()))

all_xor=a[0]
for i in range(1,N):
    all_xor=all_xor^a[i]
    
ans=[all_xor^a[i] for i in range(N)]
print(' '.join(list(map(str,ans))))