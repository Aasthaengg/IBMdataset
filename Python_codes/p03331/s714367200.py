n = int(input())

def Digits_sum(a):
    a_s = str(a)
    sum_ = 0
    for i in a_s:
        sum_ += int(i)
    return sum_

ans = 10000

for i in range(1,(n//2)+1):
    A = i
    B = n-A
    sum_ = Digits_sum(A)+Digits_sum(B)
    ans = min(ans,sum_)
print(ans)