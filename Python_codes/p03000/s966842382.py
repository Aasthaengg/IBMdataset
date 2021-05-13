n, x = list(map(int, input().split()))
l = list(map(int, input().split()))
d = [0]
for i in range(len(l)):
    d.append(d[i] + l[i])
print(len(list(filter(lambda d_i: d_i <= x, d))))