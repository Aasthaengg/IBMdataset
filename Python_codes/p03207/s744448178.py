n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
b = int(a.pop() * 0.5)
print(sum(a) + b)