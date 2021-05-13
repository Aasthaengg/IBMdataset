S = input()
n = len(S)
ans = 0

for i in range(2**(n-1)):
    mode = ['-']*(n-1)
    for j in range(n-1):
        if (i >> j) & 1 == 1:
            mode[j] = '+'
    
    val = S[0]
   
    for k in range(len(mode)):
        if mode[k] == '+':
            val += '+'
            val += S[k + 1]
        else:
            val += S[k + 1]

    ans += eval(val)
print(ans)   
