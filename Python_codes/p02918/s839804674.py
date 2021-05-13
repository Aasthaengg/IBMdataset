n, k = map(int, input().split())
s = input()
point = 0
tmp = 'N'
for i in s:
    if i == tmp: point += 1
    tmp = i
rl = s.count('RL')
lr = s.count('LR')
print(point + min(2 * k, rl + lr))