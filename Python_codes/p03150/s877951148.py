S = input()
k = "keyence"

if S == k:
    print("YES")
else:
    ans = "NO"
    s = S
    for i in range(8):
        S = list(s)
        del S[i:i+(len(S)-7)]
        if "".join(S) in k:
            ans = "YES"
            break
    
    print(ans)