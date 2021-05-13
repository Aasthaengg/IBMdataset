N,K = map(int,input().split())
A = list(map(int,input().split()))
print((len(A)-1)//(K-1) + int(bool((len(A)-1)%(K-1))))