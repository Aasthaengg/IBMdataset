a,b = map(int, input().split())
mx = max(a,b) 
mn = min(a,b)
print(max(2 * mx - 1, mx + mn))