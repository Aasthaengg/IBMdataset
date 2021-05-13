S = input()
ansA = 0
ansB = 0
for i in range(len(S)):
    N = int(S[i])
    if N == 1:
        ansA += 1
    elif N % 2 == 0:
        ansA += N//2
        ansB += N//2
    else:
        N -= 1
        ansA += N//2+1
        ansB += N//2
if ansA == 1 and ansB == 0:
    ans = 10
else:
    ans = ansA+ansB
print(ans)
