# A - Connection and Disconnection
S = input()
K = int(input())
head = 0
head_char = S[0]
head_rec = True
tmp = 0
char = ''
ans = 0
for i in range(len(S)):
    if head_rec==True:
        if S[i]==head_char:
            head += 1
        else:
            head_rec = False
    if S[i]!=char:
        char = S[i]
        ans += tmp//2
        tmp = 0
    tmp += 1
ans += tmp//2
ans *= K
if head==len(S):
    ans = (len(S)*K)//2
elif head_char==char and (tmp*head)%2!=0:
    ans += K-1
print(ans)