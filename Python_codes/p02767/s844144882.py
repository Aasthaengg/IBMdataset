n = int(input())
X = list(map(int, input().split()))
mean_L = sum(X)//n
mean_R = mean_L+1
ans = min(sum(map(lambda x: (x-mean_L)**2, X)),
          sum(map(lambda x: (x-mean_R)**2, X)))
print(ans)
