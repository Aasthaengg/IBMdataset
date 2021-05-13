# AGC 027: A – Candy Distribution Again
n, x = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

a.sort()

answer = 0
for i in range(n - 1):
    if x - a[i] < 0:
        break
    answer += 1
    x -= a[i]

if x == a[n - 1]:
    answer += 1

print(answer)