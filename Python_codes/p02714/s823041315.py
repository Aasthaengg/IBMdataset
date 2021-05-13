n = int(input())
S = input()
ans = S.count('R') * S.count('G') * S.count('B')
for i in range(n):
    for j in range(i+1,n):
        k = 2*j-i
        if k>=n:
            continue
        if S[i]==S[j] or S[j]==S[k] or S[i]==S[k]:
            continue
        else:
            ans -=1
print(ans)