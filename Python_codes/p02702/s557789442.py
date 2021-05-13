from collections import defaultdict
s = input()
n = len(s)
target = 2019
res = 0
dic = defaultdict(int)
dic[0] = 1
s = s[::-1]
num, d = 0, 1
for char in s:
    num += int(char) * d
    num %= target
    d *= 10
    d %= target
    dic[num] += 1
for i in dic.values():
    res += i * (i -1) //2
print(res)