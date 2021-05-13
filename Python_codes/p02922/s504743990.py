A,B = map(int, input().split())
print(min(i for i in range(10**6) if 1+(A-1)*i>=B))