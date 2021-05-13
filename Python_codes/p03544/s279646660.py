l = [2, 1]
n = int(input())
for i in range(2, n):
    l.append(l[i-1] + l[i-2])
if n == 1:
    print(1)
else:
    print(l[-1] + l[-2])