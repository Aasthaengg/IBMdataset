N = list(input())
a = 0
ans = 0
old = N[0]
for i in range(1, 4):
    if N[i] == old:
        a += 1
    else:
        a = 0
    if ans < a:
      ans = a
    old = N[i]
if ans > 1:
    print('Yes')
else:
    print('No')