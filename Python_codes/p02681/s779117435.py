S = input()
T = input()
ans = 'Yes'
if len(S) + 1 == len(T):
    for i in range(len(S)):
        if S[i] != T[i]:
            ans = 'No'
else:
    ans = 'No'
    
print(ans)