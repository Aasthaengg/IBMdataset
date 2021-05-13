n = int(input())
p = list(map(int, input().split()))
c = list(range(1,n+1))
print('NO' if sum([i!=j for i,j in zip(p,c)]) > 2 else 'YES')