n = int(input())
a = list(map(int, input().split()))
count = a[0]
num = 1

for i in range(1, len(a)):
    num = num * a[i] + count
    count *= a[i]

print(count/num)
