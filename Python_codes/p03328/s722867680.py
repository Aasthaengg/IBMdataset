a,b = map(int,input().split())
n = b-a-1
h = sum(x for x in range(n+1))
print(h-a)
