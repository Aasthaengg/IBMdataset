#Anti-Adjacency
N,K = map(int,input().split())
j = N//2 + N%2
if K <= j:
    print("YES")
else:
    print("NO")