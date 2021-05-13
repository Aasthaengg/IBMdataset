n = int(input())
a = input().split()

sum_a = 0
for i in a:
    sum_a += int(i)

avg = sum_a / n

sa = []

for i in a:
    if avg - int(i) >= 0:
        sa.append(avg - int(i))
    elif avg - int(i) < 0:
        sa.append(int(i) - avg)

sa_answer = min(sa)

for i in range(len(a)):
    if sum_a / n + sa_answer == int(a[i]) or sum_a / n - sa_answer == int(a[i]):
        print(i)
        break
