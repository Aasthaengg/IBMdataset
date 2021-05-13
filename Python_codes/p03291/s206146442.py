MOD = 10 ** 9 + 7

S = [0] + list(input())
n = len(S) - 1

yet = [0] * (n+1)
a = [0] * (n+1)
ab = [0] * (n+1)
abc = [0] * (n+1)
#i番目まで見終わった後の考えられる手数

abc[n] = 1

for i in range(1,n+1):
    if S[n-i+1] == "A":
        yet[n-i] = (yet[n-i+1] + a[n-i+1]) % MOD
        a[n-i] = a[n-i+1]
        ab[n-i] = ab[n-i+1]
        abc[n-i] = abc[n-i+1]
    elif S[n-i+1] == "B":
        yet[n-i] = yet[n-i+1]
        a[n-i] = (ab[n-i+1] + a[n-i+1]) % MOD
        ab[n-i] = ab[n-i+1]
        abc[n-i] = abc[n-i+1]
    elif S[n-i+1] == "C":
        yet[n-i] = yet[n-i+1]
        a[n-i] = a[n-i+1]
        ab[n-i] = (ab[n-i+1] + abc[n-i+1]) % MOD
        abc[n-i] = abc[n-i+1]
    else:
        yet[n-i] = (yet[n-i+1] * 3 + a[n-i+1]) % MOD
        a[n-i] = (a[n-i+1] * 3 + ab[n-i+1]) % MOD
        ab[n-i] = (ab[n-i+1] * 3 + abc[n-i+1]) % MOD
        abc[n-i] = (abc[n-i+1] * 3) % MOD

print(yet[0])