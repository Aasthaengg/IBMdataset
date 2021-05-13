n = int(input())
L = list(map(int,input().split()))
ans = L[0]
for i in range(1,n):
    ans ^= L[i]
if ans == 0:
    print('Yes')
else:
    print('No')
