N = int(input())
N %= 10
ans = 0
if N == 3:
    ans = 'bon'
elif N in [0,1,6,8]:
    ans = 'pon'
else:
    ans = 'hon'
print(ans)
