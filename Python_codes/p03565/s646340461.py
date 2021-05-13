import sys
S = input()
T = input()
match_list = []
for i in range(len(S)-len(T)+1):
    is_match = True
    for j in range(len(T)):
        if S[i+j] != T[j] and S[i+j] != '?':
            is_match = False
            break
    if is_match:
        match_list.append(i)
if not match_list:
    print("UNRESTORABLE")
    sys.exit()
ans = S[:max(match_list)] + T
if len(S) > len(ans):
    ans += S[len(ans):]
print(ans.replace('?', 'a'))