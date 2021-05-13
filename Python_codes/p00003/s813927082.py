
nums = input()
lines = [[]]*nums

for x in range(nums):
    lines[x] = map(int, raw_input().split(' '))


for li in lines:
    li.sort()

for li in lines:
    if li[0]**2 + li[1]**2 == li[2]**2 :
        print 'YES'
    else:
        print 'NO'