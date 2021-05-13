# 2020/07/18
# AtCoder Beginner Contest 142 - C

# Input
n = int(input())
a = list(map(int,input().split()))
al = [0] * (n+1)

# Calc
for i in range(n):
    al[a[i]] = i+1

al.remove(0)

# Output
print(' '.join([str(j) for j in al]))
