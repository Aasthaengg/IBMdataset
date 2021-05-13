n =  int(input())
ls = []
for _ in range(n):
    a, b = map(int, input().split())
    ls.append([b,a])
ls = sorted(ls)
t=0
for i in ls:
    t += i[1]
    if t > i[0]:
        print('No')
        exit(0)
print('Yes')