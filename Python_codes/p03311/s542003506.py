# 2020/05/04
# AtCoder Beginner Contest 102 - C

# Input
n = int(input())
a = list(map(int,input().split()))
ami = list()

for i in range(n):
    ami.append(a[i] - (i+1))

ami.sort()
medi = ami[n // 2]

wk_val = 0
for j in range(n):
    wk_val = wk_val + abs(a[j]-(medi+j+1))

ans = wk_val

# Output
print(ans)
