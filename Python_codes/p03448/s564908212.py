from sys import stdin

a = int(stdin.readline().rstrip())
b = int(stdin.readline().rstrip())
c = int(stdin.readline().rstrip())
x = int(stdin.readline().rstrip())

count = 0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if 500*i + 100*j + 50*k == x: count = count + 1

print (count)

