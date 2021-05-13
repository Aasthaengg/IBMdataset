# 2020-08-30, Sun

n = int(input())
lis = sorted(list(map(int, input().split())), reverse=True)
a = 0
b = 0

for i in lis[::2]:
    a += i

for i in lis[1::2]:
    b += i

print(a - b)