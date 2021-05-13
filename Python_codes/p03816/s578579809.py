n = int(input())
a = sorted(list(map(int,input().split())))
ans = len(set(a))
s = 0
cnt = 1
pre = 0
a.append(10**9)
for x in a:
    if x != pre:
        s += (cnt+1)%2
        cnt = 1
        pre = x
    else:
        cnt += 1
s %= 2
print(ans-s)
