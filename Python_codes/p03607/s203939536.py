n = int(input())
a = [int(input()) for i in range(n)]

l = sorted(a)
same = 1
count = 0
for i in range(1, n):
    if l[i] == l[i - 1]:
        same += 1
        continue
    if same % 2 == 1:
        count += 1
    same = 1
if same % 2 == 1:
    count += 1
print(count)