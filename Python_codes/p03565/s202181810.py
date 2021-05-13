S = input()
T = input()
#区間を決める
for i in range(len(S)-len(T),-1,-1):
    S_ = S[i:i+len(T)]
    frag = 1
    for j in range(len(T)):
        if S_[j] == T[j] or S_[j] == '?' :
            #print(S_[j],T[j])
            if not j == len(T)-1:
                continue
        else:
            break
            frag = 0
        if frag == 1:
            #print(S_)
            #print(S[:i] ,T ,S[len(T)+2:])
            ans = S[0:i] + T + S[len(T)+i:]
            ans = ans.replace('?','a')
            print(ans)
            exit()
print("UNRESTORABLE")
