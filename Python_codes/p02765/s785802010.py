n,r = map(int, input().split())
if n < 10:
    k = 100*(10-n)
    s = r + k
else:
    s = r
print(s)