n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
sort_a = sorted(a)

for i in a:
    if i == sort_a[-1]:
        print(sort_a[-2])
    else:
        print(sort_a[-1])