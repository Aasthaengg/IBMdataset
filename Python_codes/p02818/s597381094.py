a, b, k = map(int, input().split())
y = min(a , k)
z = min(b ,k -y)
print(a - y,b -z)