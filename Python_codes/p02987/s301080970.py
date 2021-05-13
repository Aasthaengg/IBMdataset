s = list(input())
memo = {}
for i in s:
    if i in memo:
        memo[i] += 1
    else:
        memo[i] = 1
flag = True
for key,val in memo.items():
    if val != 2:
        flag=False
        break
if flag:
    print('Yes')
else:
    print('No')