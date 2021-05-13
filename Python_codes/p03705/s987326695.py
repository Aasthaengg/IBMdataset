n,a,b = map(int, input().split())
Min, Max = a*(n-1)+b, b*(n-1)+a
print(Max-Min+1 if Max-Min+1>0 else 0)