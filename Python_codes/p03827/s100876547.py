n = int(input())
s = input()
nums = [0]
x = 0
for i in range(n):
    if s[i] == "I":
        x += 1
    else:
        x -= 1
    nums.append(x)
print(max(nums))