n = int(input())
li = list(map(int,input().split()))

point = 0

for i in li:
    while i%2 == 0:
        i //= 2
        point += 1

print(point)