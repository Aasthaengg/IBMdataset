h, a = map(int, input().split())
c = int(h/a)
if h%a!=0:
    c+=1
print(c)