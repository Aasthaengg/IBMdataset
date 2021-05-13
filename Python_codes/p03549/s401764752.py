N, M = map(int, input().split())

a = 2**M
ans = (M*1900 + (N-M)*100)*(a-1)/(1-a**-1)
print(int(ans))