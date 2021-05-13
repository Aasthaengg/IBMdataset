# 2020/07/24
# AtCoder Beginner Contest 081 - B

# Input
n = int(input())
a = list(map(int,input().split()))

# Calc
tflg = True
ans = 0
while(tflg):
    ans = ans + 1
    for i in range(n):
        if a[i] % 2 == 1:
            ans = ans - 1
            tflg = False
            break
        else:
            a[i] = a[i] / 2

# Output
print(ans)
