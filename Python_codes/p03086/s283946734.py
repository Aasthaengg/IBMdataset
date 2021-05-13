S = list(input())

ans_s = ''
for i in range(len(S)):
    for k in range(len(S[i:])):
        cnt = 0
        for s in S[i:i+k+1]:
            if s in ['A', 'C', 'G', 'T']:
                cnt += 1
        if cnt == len(S[i:i+k+1]) and cnt >= len(ans_s):
            ans_s = S[i:i+k+1]

print(len(ans_s))
                
