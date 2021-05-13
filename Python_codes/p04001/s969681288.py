s = input()
n = len(s)

ans = 0
bit_n = n-1
for i in range(2**bit_n):
    tmp = 0
    res = int(s)
    mod = 10
    for j in range(bit_n):
        if ((i>>j)&1):
            tmp+=res%mod
            res//=mod
            mod=10
        else:
            mod*=10
    ans+=res
    ans+=tmp
print(ans)