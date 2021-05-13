d,n = map(int, input().split())
n += n // 100
print(str(n) + "00"*d)
