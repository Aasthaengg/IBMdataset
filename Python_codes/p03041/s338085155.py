a,b = map(int,input().split())
c = input()
d = c[0:b - 1]
e = c[b - 1:b]
f = c[b:a]
print(d + str.lower(e) + f)