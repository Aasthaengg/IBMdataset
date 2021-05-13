# AGC 025 A - Digits Sum
n = int(input())

def DegitSum(x):
    ans = 0
    while x > 0:
        ans += x%10
        x = x // 10
    return ans
    
res = 10**8
for a in range(1, n//2+1):
    b = n - a
    if DegitSum(a) + DegitSum(b) < res:
        res = DegitSum(a) + DegitSum(b)
        
print(res)