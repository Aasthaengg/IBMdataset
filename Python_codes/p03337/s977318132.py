a, b = map(int, input().split())
s = a+b
t = a-b
p = a*b
li = [s, t, p]
li.sort()
print(li[-1])
