n = int(input())

lst = [-1 for i in range(n)]
print(0)
sex0 = input()
if sex0 == 'Male':
    lst[0] = 1
    leftsex = 1
elif sex0 == 'Female':
    lst[0] = 0
    leftsex = 0
else:
    exit()

print(n-1)
sexn_1 = input()
if sexn_1 == 'Male':
    lst[n-1] = 1
    rightsex = 1
elif sexn_1 == 'Female':
    lst[n-1] = 0
    rightsex = 0
else:
    exit()

left = 0
right = n-1
while left+1 < right:
    mid = (left+right)//2
    print(mid)
    sexmid = input()
    if sexmid == 'Male':
        lst[mid] = 1
        midsex = 1
    elif sexmid == 'Female':
        lst[mid] = 0
        midsex = 0
    else:
        exit()
    
    if (mid-left) % 2 == abs(midsex-leftsex):
        left = mid
        leftsex = midsex
    else:
        right = mid
        rightsex = midsex