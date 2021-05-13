n = int(input())
a = [input() for i in range(n)]

l = sorted(a)

count = 1
for i in range(n - 1):
    if l[i] != l[i + 1]:
        count += 1
    
print(count)