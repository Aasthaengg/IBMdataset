N = int(input())
p = [int(input()) for i in range(0,N,1)]
p.sort()
p[N-1]=p[N-1]//2
print(sum(p))