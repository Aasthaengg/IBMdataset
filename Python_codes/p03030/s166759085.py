n = int(input())
l = []
for i in range(n):
    x, y = input().split()
    l.append([i+1, x, -int(y)])
l = sorted(l, key=lambda x:(x[1],x[2]))

for i in l:
    print(i[0])