import sys

S = sys.stdin.readline().strip()
changed = 0
for i in range(len(S) - 1):
    if S[i] != S[i+1]:
        changed += 1

print(changed)