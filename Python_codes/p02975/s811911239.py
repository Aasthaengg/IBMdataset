n = int(input())
l = list(map(int, input().split()))
k = l[0]
for i in l[1:]:
    k ^= i
if k != 0:
    print('No')
else:
    print('Yes')
