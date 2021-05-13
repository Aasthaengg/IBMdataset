# A - Kenken Race

N,A,B,C,D = map(int,input().split())
S = input()

should_change = int(C>D)
can_change = 0
space = 1
ans = 'Yes'

for i in range(A,max(C,D)):
    if S[i]=='.':
        space += 1
        if B<=i<=D and space==3:
            can_change = 1
    else:
        if space==0:
            ans = 'No'
            break
        space = 0

if can_change<should_change:
    ans = 'No'
print(ans)