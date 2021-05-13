alp = "abcdefghijklmnopqrstuvwxyz"
s = input()
K = int(input())
N = len(s)
T = ""
for i in range(N):
    n = alp.index(s[i])
    if i==N-1:
        T+=alp[(n+K)%26]
    else:
        if n!=0 and K>=26-n:
            T+="a"
            K-=(26-n)
        else:T+=alp[n]
print(T)