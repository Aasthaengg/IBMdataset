# 2020/05/02
# AtCoder Grand Contest 029 - A

# Input
s = input()

sidx = len(s) - 1
bidx = -1
ans = 0
leftflg = True
while(sidx >= 0):
    # Set Init position of B
    if leftflg and s[sidx] == 'W':
        leftflg = False
        bidx = sidx
    # Put B
    elif s[sidx] == 'B':
        ans = ans + max(0, bidx - sidx) 
        bidx = bidx - 1
        
    sidx = sidx - 1

# Output
print(ans)
