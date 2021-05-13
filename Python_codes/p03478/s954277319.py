def digit_sum(x): 
    y = str(x) 
    y_len = len(y) 
    ans = 0
    for j in range(y_len):
        ans += int(y[j]) 

    return ans

answer=0
n,a,b = map(int,input().split()) 
for i in range(1, n+1):
    if a<= digit_sum(i) <= b:
        answer+=i

print(answer)