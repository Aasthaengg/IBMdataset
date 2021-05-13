S = input()
K = int(input())

rest = K
oz = ord('z')
oa = ord('a')
ans = list(S)

for ci in range(len(S)):
    if S[ci] == 'a':
        continue
    
    check = oz - ord(S[ci]) + 1
    if rest >= check:
        ans[ci] = 'a'
        rest -= check

if rest >= 0:
    for i in range(rest%26):
        if oz == ord(ans[-1]):
            ans[-1] = 'a'
        else:
            ans[-1] = chr(ord(ans[-1])+1)
    
print("".join(ans))

