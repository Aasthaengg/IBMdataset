n, k = map(int, input().split())
r,s,p = map(int, input().split())
t = list(input())

lis = []
for i in t:
    if i == 'r':
        lis.append('p')
    elif i == 's':
        lis.append('r')
    else:
        lis.append('s')

ans1 = 0
for i in range(k, len(lis)):
    if lis[i] == lis[i-k]:
        lis[i] = 'o'

rc = lis.count('r') * r
sc = lis.count('s') * s
pc = lis.count('p') * p

print(rc+sc+pc)