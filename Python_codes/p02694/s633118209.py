import sys
X = int(input())

if not ( 101 <= X <= 10**18 ): sys.exit()

base = 100
count = 0
while base < X:
    base += base // 100
    count += 1

print(count)