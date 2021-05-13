S = input()
s = len(S)-1
ans=0
for bit in range(1 << s):
    a = S[0]
    for i in range(s):
        if bit & (1<<i):
            a += "+"
        a += S[i+1]
    ans += sum(map(int,a.split("+")))
print(ans)
