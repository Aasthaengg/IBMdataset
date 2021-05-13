N, K = map(int,input().split())
print(pow(N//K,3)+(1-K%2)*pow((N+(K//2))//K,3))
