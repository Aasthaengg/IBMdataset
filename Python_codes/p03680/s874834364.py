n = int(input())
l = [-1]
for i in range(n):
    l.append(int(input()))
x = 1
for i in range(n):
    if l[x] == 2:
        print(i+1)
        exit()
    x = l[x]
if x != 2:
    print(-1)
