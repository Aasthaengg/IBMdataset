def cal(debt,n):
    if n==0: return debt
    for i in range(n):
        debt=debt*1.05
        if debt/1000>int(debt/1000):
            debt=(int(debt/1000)+1)*1000
    return debt

debt=100000
n=int(input())
print(cal(debt,n))