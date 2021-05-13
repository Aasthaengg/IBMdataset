s = sorted(list(map(int, input().split())))
a = s.pop(-1)
b = a // 2
c = a - (a//2)
d = s[0] * s[1]
print(abs(d * b - d * c))