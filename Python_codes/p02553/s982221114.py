data = list(map(int,input().split()))
a = data[0]
b = data[1]
c = data[2]
d = data[3]
data[0] = a*c
data[1] = a*d
data[2] = b*c
data[3] = b*d
print(max(data))