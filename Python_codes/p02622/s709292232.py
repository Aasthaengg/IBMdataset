S = input()
T = input()
ans = 0
for count, i in enumerate(T):
    if(S[count] != i):
        ans = ans + 1
print(ans)
