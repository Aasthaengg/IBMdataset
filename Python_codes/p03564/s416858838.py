n = int(input())
k = int(input())
l = [1]
for i in range(n):
    l = [i * 2 for i in l] + [i + k for i in l]
print(min(l))