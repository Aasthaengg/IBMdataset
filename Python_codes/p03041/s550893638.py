n,k = map(int, input().split())
s = list(input())
r = s[k-1].lower()
del s[k-1]
s.insert(k-1, r)
S = ''.join(s)
print(S)