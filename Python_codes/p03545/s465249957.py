import sys

tmp = list(sys.stdin.readline().strip())
nums = list(map(int, tmp))

for a in range(2):
    for b in range(2):
        for c in range(2):
            tmp = nums[0]
            exp = str(nums[0])
            if a == 0:
                tmp += nums[1]
                exp += "+"
            else:
                tmp -= nums[1]
                exp += "-"
            exp += str(nums[1])
            if b == 0:
                tmp += nums[2]
                exp += "+"
            else:
                tmp -= nums[2]
                exp += "-"
            exp += str(nums[2])
            if c == 0:
                tmp += nums[3]
                exp += "+"
            else:
                tmp -= nums[3]
                exp += "-"
            exp += str(nums[3])
            if tmp == 7:
                print(exp + "=7")
                sys.exit()