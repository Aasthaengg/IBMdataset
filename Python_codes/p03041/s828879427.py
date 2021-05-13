N,K = map(int,input().split())
S = input()
s = list(S)
T = s[K-1]
T = T.lower()
s[K-1] = T
s = ''.join(s)
print(s)