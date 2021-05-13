N = int(input())
a = list(map(int,input().split()))

x = 0
count = 0

for i in range(N):
    a_number = a[i]
    while a_number % 2 == 0:
        a_number = a_number // 2
        count += 1
print(count)