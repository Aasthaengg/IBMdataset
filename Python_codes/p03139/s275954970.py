n,a,b = map(int, input().split())

both = min(a,b)
any = max(0, (a+b) - n)

print(both, any)