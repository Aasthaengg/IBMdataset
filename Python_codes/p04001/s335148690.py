S = input()
N = len(S) - 1
 
ans = 0
for i in range(2 ** N):
    equation = ""
    for j in range(N):
        equation += S[j]
        if (i >> j) & 1:
            equation += "+"
    equation += S[N]
    ans += sum(list(map(int, equation.split("+"))))
 
print(ans)