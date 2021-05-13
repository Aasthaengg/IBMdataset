h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

l = []
for i in range(n):
    for _ in range(a[i]):
        l.append(i+1)

ans = []
flag = True
for i in range(h):
    if flag:
        ans.append(l[w*i:w*(i+1)])
    else:
        ll = l[w*i:w*(i+1)]
        ll.reverse()
        ans.append(ll)
    flag = not flag

for i in ans:
    print(' '.join(map(str, i)))