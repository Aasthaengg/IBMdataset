d,n = map(int, raw_input().split())
print (n + (1 if n == 100 else 0)) * (100 ** d)
