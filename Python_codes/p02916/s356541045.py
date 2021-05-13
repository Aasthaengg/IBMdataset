# ABC 140

N = int(input())
A = [int(a)-1 for a in input().split()]
B = [int(a) for a in input().split()]
C = [int(a) for a in input().split()]
m =0
l = N + 10
for a in A:
    m+=B[a]
    if l+1 == a:
        m+=C[l]
    l=a
print(m)