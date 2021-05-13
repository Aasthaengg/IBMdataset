a = int(input())
b = a // 3600
c = a - b * 3600
d = c // 60
A = a - b * 3600 + d * 60
B = A % 60
print(str(b) + ":" + str(d) + ":" + str(B))

