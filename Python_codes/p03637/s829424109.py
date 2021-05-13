N = int(input())
nums = list(map(int, input().split()))

d4 = 0
d2 = 0
d0 = 0
for n in nums:
    if n % 4 == 0:
        d4 += 1
    elif n % 2== 0:
        d2 += 1
    else:
        d0 += 1

if d2 > 0 and d0 <= d4:
    print('Yes')
elif d2 == 0 and d0 <= d4+1:
    print('Yes')
else:
    print('No')