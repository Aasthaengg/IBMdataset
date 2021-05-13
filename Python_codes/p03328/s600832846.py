a,b = map(int,input().split())
n = b-a
right = sum(list(range(1,n+1)))
print(right - b)