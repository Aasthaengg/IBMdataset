n = int(input())
l = list(range(1, n+1))
for i in range(len(l)):
    if l[i] % 3 == 0 or l[i] % 5 == 0:
        l[i] = 0

print(sum(l))
