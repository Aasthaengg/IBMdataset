n = int(input())
a = [int(i) for i in input().split()]
l = [0]*(n+1)
for i in a:
    l[i] += 1

for i in l[1:]:
    print(i)