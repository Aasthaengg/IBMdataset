import math

x = int(input())
ans = [1]
s = int(math.sqrt(x))
if s >= 2:
    for i in range(2,s+1):
        temp = i
        while True:
            temp *= i
            if temp <= x:
                ans.append(temp)
            else:
                break

print(max(ans))