S = input()

n = len(S)
Slen = 2**(n-1)
ans = 0

for i in range(Slen):
    Slis = S[0]
    for j in range(n-1):
        if i &(1 << j):
            Slis += "+"
        Slis += S[j+1]
    ans += sum(map(int,Slis.split("+")))

print(ans)
