n = int(input())
C = [x for x in str(input())]
cnt_R = C.count('R')
swap_W = C[:cnt_R].count('W')
ans = swap_W
print(ans)