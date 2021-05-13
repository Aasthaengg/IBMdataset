S = input()
X = S[0]
ans = 0
while 1:    
    for i in range(len(S)):
        if S[i] != X:
            ans += 1
            X =S[i]
            S = S[i:]
            break
    else:
        break
print(ans)
    
