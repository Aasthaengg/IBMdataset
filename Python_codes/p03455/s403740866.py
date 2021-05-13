nums = list(map(int, input().split()))
a, b = nums[0], nums[1] 

if (a * b) % 2 == 1 :
    print('Odd')
else :
    print('Even')