nums = input().split()
W = int(nums[0])
H = int(nums[1])
X = int(nums[2])
Y = int(nums[3])
R = int(nums[4])
if (X - R) >= 0 and (X + R) <= W:
    if (Y - R) >= 0 and (Y+ R) <= H:
        print("Yes")
    else:
        print("No")
else:
    print("No")