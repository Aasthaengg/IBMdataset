# 140 B

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
sum = 0

for i in range(len(a)):
    sum += b[a[i] - 1]
    try:
        if i != 0 and a[i] == a[i-1] + 1:
           sum += c[a[i-1] - 1]
    except IndexError:
        continue

print(sum)