# 2020/07/04
# AtCoder Beginner Contest 071 - C

# Input
n = int(input())
a = list(map(int,input().split()))

a.sort()

h_long = 0
h_short = 0
i = n - 1

#for i in range(n-1, 0, -1):
while i > 0:
    if a[i-1] == a[i]:
        if h_long == 0:
            h_long = a[i]
            i = i - 1
        else:
            h_short = a[i]
            break
    i = i - 1

ans = h_short * h_long

# Output
print(ans)
