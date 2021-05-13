N = int(input())
powlist = []
for i in range(7):
    powlist.append(2 ** i)
ans = 1
for p in powlist:
    if N >= p:
        ans = p
print(ans)