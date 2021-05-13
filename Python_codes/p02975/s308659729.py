N = int(input())
a = list(map(int,input().split()))
num = a[-1]
for i in range(N-1):
    num = num^a[i]
if num == 0:
    print('Yes')
else:
    print('No')