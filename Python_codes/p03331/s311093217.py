def digit_sum(x): 
    y = str(x) 
    y_len = len(y) 
    ans = 0
    for j in range(y_len):
        ans += int(y[j]) 

    return ans

answer = 10**8 
n = int(input()) 
for i in range(1,n):
    a = i 
    b = n - a 
    answer = min(answer, digit_sum(a)+ digit_sum(b))

print(answer)