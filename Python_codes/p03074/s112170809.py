N, K = map(int, input().split())
S = input()

zero_list = []
for i in range(N):
    if S[i] == '0':
        if i > 0 and S[i - 1] == '0':
            zero_list[-1][0] += 1
            zero_list[-1][2] += 1
        else:
            zero_list.append([1, i, i])
            
if len(zero_list) <= K:
    ans = N
else:
    zero_c_max = zero_list[K][1]
    l = 0
    r = zero_list[K][1] - 1
    for j in range(1, len(zero_list) - K + 1):
        l = zero_list[j - 1][2] + 1
        if j + K < len(zero_list): 
            r = zero_list[j + K][1] - 1
        else:
            r = N - 1
        if (r - l) + 1 > zero_c_max:
            zero_c_max = (r - l) + 1
    
    ans = zero_c_max
    
print(ans)