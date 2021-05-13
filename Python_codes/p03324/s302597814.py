d,n = map(int,input().split())
if n == 100:
    n = 101
print(str(n)+str(100**d)[1:])