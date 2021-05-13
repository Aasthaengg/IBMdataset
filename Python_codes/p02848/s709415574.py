import string
l = string.ascii_uppercase

N = int(input())
S = input()

ans = []
for c in S :
    plusNumber = (l.index(c) + N) % 26
    ans.append(l[plusNumber])
print("".join(ans))