split = input().split()
a = int(split[0])
b = int(split[1])
c = int(split[2])
nums = []

check = a if a < b else b

for i in range(1, check + 1, 1):
    if a % i == 0 and b % i == 0:
        nums.append(i)
print(nums[-c])