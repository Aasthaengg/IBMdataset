s = list(map(int, input().split()))
ss = sorted(s)
print(sum(s)-ss[1]*2)