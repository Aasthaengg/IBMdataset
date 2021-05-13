n = input()
a = map(int, raw_input().split())
a.sort()
sum = 0
for i in range(len(a)):
    sum += a[i]
print("%d %d %d" %(a[0], a[len(a) - 1], sum))