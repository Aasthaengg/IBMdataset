# 2020/04/25
# CODE FESTIVAL 2016 Final - B

# Input
n = int(input())

# Calc
wk_val = 0

x = 1
# while (x*(x+1)) / 2 <= n:
while (x*(x+1)) / 2 < n:
    x = x + 1

wk_ans = 0
anslist = list()
while(x > 0):
    if wk_ans + x <= n:
        wk_ans = wk_ans + x
        anslist.append(x)

    if wk_ans == n:
        break
    
    x = x - 1

# Output
for i in range(len(anslist)):
    print(anslist[i])
