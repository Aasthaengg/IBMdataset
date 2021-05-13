N = int(input())
S= [input() for _ in range(N)]
nums = [0]*5
for s in S:
    if s[0] == 'M':
        nums[0] += 1
    elif s[0] == 'A':
        nums[1] += 1
    elif s[0] == 'R':
        nums[2] += 1
    elif s[0] == 'C':
        nums[3] += 1
    elif s[0] == 'H':
        nums[4] += 1
c = 0
for i in range(3):
    for j in range(i+1,4):
        for k in range(j + 1, 5):
            c += nums[i]*nums[j]*nums[k]
print(c)




