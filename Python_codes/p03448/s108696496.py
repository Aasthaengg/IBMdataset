#500円玉
a = int(input())
#100円玉
b = int(input())
#50円玉
c = int(input())
#50の倍数
x = int(input())

h = 0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            y = 500*i + 100*j + 50*k
            if x == y:
                h += 1
print(h)

