n = int(input())
ls = list(map(int,input().split()))
p = 0
for i in ls:
    while i % 2 == 0:
        i = i/2
        p += 1
print(p)