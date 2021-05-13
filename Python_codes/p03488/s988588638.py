import datetime
s = input()
x, y = map(int, input().split())
#print(datetime.datetime.now())
 
num_of_f = 0
for c in s:
    if c == 'F':
        num_of_f += 1
dp = [[[False] * 32001 for _ in range(2)] for _ in range(2)]
 
dp[0][0][0] = True
dp[0][1][0] = True
# print(dp)
index = 0
while index < len(s) and s[index] == 'F':
    index += 1
x -= index
xy_axis = 1
dp_index = 1
i = index + 1
num_of_f = index
while i < len(s):
    num = 0
    while i < len(s) and s[i] == 'F':
        num += 1
        i += 1
    num_of_f += num
    for j in range(-1 * num_of_f, num_of_f + 1):
        dp[dp_index][xy_axis][j] = dp[(dp_index + 1) % 2][xy_axis][j - num] or dp[(dp_index + 1) % 2][xy_axis][j + num]
    xy_axis = (xy_axis + 1) % 2
    if xy_axis == 1:
        dp_index = (dp_index + 1) % 2
    i += 1
 
# print(dp)
 
if dp[(dp_index + 1) % 2][0][x] and dp[(dp_index + xy_axis) % 2][1][y]:
    print('Yes')
else:
    print('No')
#print(datetime.datetime.now())