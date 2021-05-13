def divide_2(n):
    count = 0
    while n % 2 == 0:
        n /= 2
        count += 1
    return count


n = int(input())
a = list(map(int, input().split()))

control_count = 0
for i in range(n):
    control_count += divide_2(a[i])
print(control_count)
