N,K = map(int,input().split())
x=list(map(int,input().split()))

d= [x[i+K-1]-x[i] + min(abs(x[i+K-1]),abs(x[i]) )   for i in range(N-K+1)]

print(min(d))