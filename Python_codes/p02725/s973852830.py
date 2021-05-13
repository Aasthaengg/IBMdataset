K,N = map(int,input().split())
A = list(map(int,input().split()))

l = [ A[i+1]-A[i] for i in range(N-1)]
l.append( K-A[-1] + A[0] )

l.remove(max(l))
print(sum(l))