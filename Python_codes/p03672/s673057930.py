S = input()
N = len(S)
for i in range(len(S)):
    S = S[0:-1]
    if len(S)%2 == 0:
        if S[0:len(S)//2] == S[len(S)//2:len(S)]:
            ans = i+1
            break
    else:
        pass
print(N - ans)