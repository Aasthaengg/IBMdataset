k, t = map(int, input().split())
a = sorted(map(int, input().split()))
mv = a[-1]
nmv = sum(a[:-1])
# print(mv, nmv)
if nmv+1 <= mv:
    print(mv - nmv - 1)
else:
    print(0)