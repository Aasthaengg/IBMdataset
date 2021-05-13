N, L = map(int, input().split())
tsum = (1+N)*N/2 + (L-1)*N
apple = [abs(L+i-1) for i in range(1, N+1)]
a = apple.index(min(apple))
print(int(tsum-(a+L)))