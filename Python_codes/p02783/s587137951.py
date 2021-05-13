h,a = map(int,input().split())
if h%a == 0:
    result = int(h/a)
else:
    result = int(h/a) + 1
print(result)