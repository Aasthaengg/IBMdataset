n, *a_l= map(int, open(0).read().split())
cnt = 0
for i, a in enumerate(a_l):
    if a_l[a-1] == i+1:
        cnt += 1
print(cnt//2)