from numpy import sqrt, round
a, b = input().split(' ')
ans = sqrt(int(a + b))
if ans == round(ans):
    print('Yes')
else:
    print('No')