S_list = [int(input()) for i in range(4)]

n, k, x, y = S_list
if n>=k:
    result = k*x +(n-k)*y    
else:
    result = n*x
print(result)