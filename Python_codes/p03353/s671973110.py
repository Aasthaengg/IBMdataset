import sys
input = sys.stdin.readline
S = set()
s = list(input().rstrip())
K = int(input())
for i in range(len(s)):
    for j in range(i+1, i+K+1):
        if "".join(s[i:j]) not in S:
            S.add("".join(s[i:j]))
S = list(S)
S.sort()
print("".join(S[K-1]))
