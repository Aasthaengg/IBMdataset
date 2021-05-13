a, b = map(int, input().split())
x = (a+b)/2
# print(x)
m, n = divmod(x,1)
# print("{},{}".format(m,n))
if n>0:
    ans = m+1
else:
    ans = m
print(int(ans))