n = int(input())
s = [2, 1]
for i in range(n - 1):
    s.append(s[-1] + s[-2])
print(s[-1])