import sys

S = input()
target = "keyence"
del_len = len(S) - len(target)

for i in range(len(S) - del_len+1):
    s = S[:i] + S[i + del_len:]
    if s==target:
        print("YES")
        sys.exit()
print("NO")