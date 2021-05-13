N = int(input())
S = input()
ans = "Yes"
if N % 2 != 0:
    ans = "No"
else:
    x = N//2
    for i in range(x):
        if S[i] != S[i+x]:
            ans = "No"
            break
print(ans)
