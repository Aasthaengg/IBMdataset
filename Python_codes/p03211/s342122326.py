S = input()
ans = 99999
ans_s = 99999
for i in range(0,len(S)-2):
    s = int(S[i:i+3])
    ans = min(ans,abs(s-753))
    
print(ans)