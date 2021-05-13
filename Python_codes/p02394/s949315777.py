
nums = map(int, raw_input().split())
WH = [nums[0], nums[1]]
xy = [nums[2], nums[3]]
r  = nums[4]

up    = xy[1] + r
low   = xy[1] - r
right = xy[0] + r
left  = xy[0] - r

if up > WH[1] or low < 0 or right > WH[0] or left < 0:
    print "No"
else:
    print "Yes"