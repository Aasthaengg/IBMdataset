n = int(input())
a = list(input())
b = list(input())
c = list(input())
cnt = 0

for x,y,z in zip(a,b,c):
    if x == y == z:
        continue
    elif x == y or y == z or z == x:
        cnt += 1
    else:
        cnt += 2

print(cnt)