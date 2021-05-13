n = int(input())
a = list(map(int,input().split()))

s = sum(a)

start = s-2*sum(a[1::2])

li = [start]

for i in range(1,n):
    li.append(2*a[i-1]-li[-1])

print(*li)