N,M = [int(i) for i in input().split()]
ans = ((N-M)*100+M*1900)*2**M
print(ans)