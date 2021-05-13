#template
def inputlist(): return [int(j) for j in input().split()]
def listinput(): return input().split()
#template
K,N = inputlist()
A = inputlist()
dis = [0]*(N)
for i in range(N):
    if i == N-1:
        dis[i] = K+A[0] - A[i]
        continue
    dis[i] = A[i+1] - A[i]
dis.sort()
print(sum(dis[:-1]))