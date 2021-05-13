#2 Kleene Inversion
n,k=map(int,input().split())
a=list(map(int,input().split()))
mod=10**9+7

a_out = [sum(bb > aa for bb in a ) for aa in a]
a_in = [sum(a[i] > a[j] for i in range(n) if i<j) for j in range(n)]

print( (sum(a_out)*k*(k-1)//2 + sum(a_in)*k)%mod )