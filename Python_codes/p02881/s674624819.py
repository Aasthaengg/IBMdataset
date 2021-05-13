import math
n = int(input())
root = int(math.sqrt(n))
ans = []
for i in range(1,root+1):
    if n%i == 0:
        tmp = i-1 + (n//i)-1
        ans.append(tmp)
print(min(ans))