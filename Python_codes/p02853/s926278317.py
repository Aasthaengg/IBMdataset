X,Y = map(int,input().split())
ans = max(4-X, 0) + max(4-Y, 0)
print(ans * 10**5 if ans != 6 else 10**6)