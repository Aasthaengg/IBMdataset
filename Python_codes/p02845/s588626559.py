N,*A = map(int, open(0).read().split())
group = [0] * 3
ans = 1
for x in A:
    ans = (ans*group.count(x)) % 1000000007
    if ans == 0:
        print(0)
        break
    else:
        group[group.index(x)] += 1
else:
    print(ans)