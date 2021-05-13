import sys
def S(): return sys.stdin.readline().rstrip()
S = S()
ans,target_index = 0,0
for i in range(len(S)):
    if S[i]=='W':
        ans += i-target_index
        target_index += 1
print(ans)
