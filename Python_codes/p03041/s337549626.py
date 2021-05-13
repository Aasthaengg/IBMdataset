N, K = map(int, input().split())
S = input()

Sstr = list(S)
Sstr[K-1] = Sstr[K-1].lower()
S2 = ''.join(Sstr)

print(S2)