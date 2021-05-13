n = int(input())
s = input()

res = 1 << 40
num_black = 0
num_white = s.count('.')
for i in range(n):
    res = min(res, num_black + num_white)
    if s[i] == '.':
        num_white -= 1
    else:
        num_black += 1
        
res = min(res, num_black + num_white)
print(res)