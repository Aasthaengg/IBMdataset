N, M = map(int, input().split())
ans = (100*(N-M)+1900*M)*pow(2,M)
print(ans)