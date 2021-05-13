n,m = map(int, input().split())
a = list(map(int, input().split()))
num = 0
for i in a:
    if 1/(4*m) <= i/sum(a):
        num += 1
if m <= num:
    print('Yes')
else:
    print('No')