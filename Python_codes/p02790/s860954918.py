a, b = map(int, input().split())
if int(str(a)*b) <= int(str(b)*a):
    print(str(b)*a)
else:
    print(int(str(a)*b))