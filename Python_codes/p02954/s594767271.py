import sys
sys.setrecursionlimit(10**6)

s = input()

ans = [0]*len(s)

i = 0
len_left = 1
len_right = 0
intersec_left = 0
now_left = True

while i < len(s)-1:
    if s[i] == s[i+1] and now_left:
        len_left += 1
    elif s[i] != s[i+1] and now_left:
        len_right += 1
        intersec_left = i
        now_left = False
    elif s[i] == s[i+1]:
        len_right += 1
    else:
        if len_left%2 == 0:
            ans[intersec_left] += len_left//2
            ans[intersec_left+1] += len_left//2
        else:
            ans[intersec_left] += len_left//2+1
            ans[intersec_left+1] += len_left//2
        if len_right%2 == 0:
            ans[intersec_left] += len_right//2
            ans[intersec_left+1] += len_right//2
        else:
            ans[intersec_left] += len_right//2
            ans[intersec_left+1] += len_right//2+1
        len_left = 1
        len_right = 0
        intersec_left = i+1
        now_left = True
    i += 1
else:
    if len_left%2 == 0:
        ans[intersec_left] += len_left//2
        ans[intersec_left+1] += len_left//2
    else:
        ans[intersec_left] += len_left//2+1
        ans[intersec_left+1] += len_left//2
    if len_right%2 == 0:
        ans[intersec_left] += len_right//2
        ans[intersec_left+1] += len_right//2
    else:
        ans[intersec_left] += len_right//2
        ans[intersec_left+1] += len_right//2+1
    
print(*ans)