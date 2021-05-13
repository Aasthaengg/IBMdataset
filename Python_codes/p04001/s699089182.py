n = list(input())
ans = 0
for i in range(2**(len(n)-1)):
    plus = [""]*(len(n))
    fomula = ""
    for j in range(len(n)-1):
        if(i>>j & 1):
            plus[j] = "+"
    for i in range(len(n)):
        fomula += n[i] + plus[i]
    ans += eval(fomula)
print(ans)

