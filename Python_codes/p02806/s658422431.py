n = int(input())
li_s = list()
for i in range(n):
    li_s.append(tuple(input().split()))
x = input()

sum = 0
for idx, v in enumerate(li_s):
    sum += int(v[1])
    if v[0] == x:
        sum = 0
print(sum)
