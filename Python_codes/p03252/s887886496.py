import sys
S = input()
T = input()
tmp1 = [set() for i in range(26)]
tmp2 = [set() for i in range(26)]
alpha2num = lambda c: ord(c) - ord('a')
for i in range(len(S)):
    tmp1[alpha2num(S[i])].add(T[i])
    tmp2[alpha2num(T[i])].add(S[i])
for i in range(26):
    if len(tmp1[i]) > 1 or len(tmp2[i]) > 1:
        print("No")
        sys.exit()
print("Yes")
