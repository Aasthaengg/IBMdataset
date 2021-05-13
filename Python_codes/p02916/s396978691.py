n = int(input())
jun = [int(s) for s in input().split()]
r = [int(s) for s in input().split()]
m = [int(s) for s in input().split()]

point = 0
for i in range(n):
    point += r[jun[i]-1]
    if jun[i]-1 == jun[i-1] and i > 0:
        point += m[jun[i-1]-1]
print(point)