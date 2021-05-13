n = int(input())
a = 0
for i in range(1, n+1):
    if len(list(str(i))) % 2 == 1:
        a += 1
print(a)
