N = str(input())
Sta = 753
Ans = 1000

for i in range(len(N)-2):
    C_Ans = abs(Sta-int("".join(N[i:i+3])))
    if C_Ans < Ans:
        Ans = C_Ans

print(Ans)