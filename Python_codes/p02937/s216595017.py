from bisect import bisect_right

s = input()
t = input()
obj = {}

loop_num = 0
temp_num = -1

for i in range(len(s)):
    char = s[i]
    if not (char in obj):
        obj[char] = [i]
    else:
        obj[char].append(i)

for i in range(len(t)):
    char = t[i]
    if not (char in obj):
        loop_num = -1
        break
    else:
        next_index = bisect_right(obj[char], temp_num)
        if next_index == len(obj[char]):
            loop_num += 1
            temp_num = obj[char][0]
        else:
            temp_num = obj[char][next_index]

if(loop_num == -1):
    print(-1)
else:
    print(loop_num * len(s) + temp_num + 1)