a,b = map(int,input().split())
c = list(map(int,input().split()))
ans = -(-(a - b) // (b - 1)) + 1
print(ans)


