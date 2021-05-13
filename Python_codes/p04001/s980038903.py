S = input()
S_str = str(S)
n = len(str(S))
ans = 0

for i in range(2**(n-1)):
    tmp = 0
    for j in range(n-1):
        if i & (1 <<(n-2 -j)):
            ans += 10*tmp + int(S_str[j])
            tmp = 0
        else:
            tmp = 10*tmp + int(S_str[j]) 
    ans += 10*tmp + int(S_str[-1])
print(ans)