n = int(input())
S = [input() for i in range(n)]

ans = 0
a_cnt = 0
b_cnt = 0
ba_cnt = 0
for i in range(n):
    ans+=S[i].count('AB')
    if S[i][0]=='B' and S[i][-1]=='A':
        ba_cnt+=1
    elif S[i][-1]=='A':
        a_cnt+=1
    elif S[i][0]=='B':
        b_cnt+=1

print(ans+min(a_cnt,b_cnt)+ba_cnt-1*(ba_cnt>0 and a_cnt==b_cnt==0))