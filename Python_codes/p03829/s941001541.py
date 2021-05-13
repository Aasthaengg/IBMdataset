from sys import stdin

n,a,b = [int(x) for x in stdin.readline().rstrip().split()]
li = list(map(int,stdin.readline().rstrip().split()))

point = 0
for i in range(n-1):
    if (li[i+1]-li[i])*a < b:
        point += (li[i+1]-li[i])*a
    else:
        point += b

print(point)