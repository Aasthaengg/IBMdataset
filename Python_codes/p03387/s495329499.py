import sys
input = sys.stdin.readline

num = list(map(int,input().split()))
num.sort()
dif1 = num[2] - num[1]
dif2 = num[2] - num[0]

if (dif2 - dif1) % 2 == 0:
    ans = dif1 + (dif2-dif1)//2
else:
    ans = dif1 + (dif2-dif1+1)//2 + 1

print(ans)
