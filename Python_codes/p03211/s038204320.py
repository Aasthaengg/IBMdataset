S = list(input())

ans = 753

for i in range(len(S)-2):
    sa = abs(753-(int(S[i])*100 + int(S[i+1])*10 + int(S[i+2])))
    ans = min(sa,ans)
             
print(ans)