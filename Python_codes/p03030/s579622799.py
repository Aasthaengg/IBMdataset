n = int(input())

l = []

for i in range(n):
    s, p = map(str, input().split())
    p = int(p)
    l.append([s, -p, i+1])

l.sort()

for _, _, i in l:
    print(i)
