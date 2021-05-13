n = int(input())

a = [int(input()) for i in range(n)]

b = []
flag = 0
for i in a:
    if i == max(a) and flag == 0:
        b.append(i/2)
        flag = 1
    else:
        b.append(i)

print(int(sum(b)))