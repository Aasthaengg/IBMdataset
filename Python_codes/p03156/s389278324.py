n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))
c = [0, 0, 0]
for pt in p:
    if pt > b:
        c[2] += 1
    elif pt > a:
        c[1] += 1
    else:
        c[0] += 1
print(min(c))