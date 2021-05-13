#B - Exponential
import math
X = int(input())
def expo(x):
    ans = 1
    for i in reversed(range(1,x+1)):
        for j in range(int(math.sqrt(x))+1):
            for k in range(2,int(math.sqrt(x))):
                if i == j**k:
                    ans = i
                    return ans
    return ans
print(expo(X))