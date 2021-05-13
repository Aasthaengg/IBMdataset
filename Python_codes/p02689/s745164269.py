n,m = map(int,input().split())
h = list(map(int,input().split()))
A = []
B = []
h_new = [0]*n
c = 0
for i in range(m):
    a,b = map(int,input().split())
    A += [a]
    B += [b]
    
for i in range(m):
    h_new[A[i]-1] = max(h[B[i]-1],h_new[A[i]-1])
    h_new[B[i]-1] = max(h_new[B[i]-1],h[A[i]-1])
    
for i in range(n):
    if h[i] > h_new[i]:
        c += 1
print(c)