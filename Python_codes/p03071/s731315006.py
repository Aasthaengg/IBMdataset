A,B = map(int,input().split())
x = max(A,B)
x += max(x-1,min(A,B))
print(x)