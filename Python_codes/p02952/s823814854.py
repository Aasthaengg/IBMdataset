import sys
N = int(input())
Nlen = len(str(N))
ans = 0
if Nlen == 1:
    ans = N
elif Nlen == 2:
    ans = 9
elif Nlen == 3:
    ans = 9+N-99
elif Nlen == 4:
    ans = 9+900
elif Nlen == 5:
    ans = 9+900+N-9999
elif Nlen == 6:
    ans = 9+900+90000
print(ans)
