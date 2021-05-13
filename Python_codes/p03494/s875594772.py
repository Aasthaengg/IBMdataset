n = int(input())
a = list(map(int, input().split()))
l = [0 for i in range(n)]
for i in range(len(a)):
    while a[i] % 2 == 0:
        a[i] /= 2
        l[i] += 1
print(min(l))