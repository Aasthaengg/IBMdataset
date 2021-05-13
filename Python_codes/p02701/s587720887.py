N = int(input())
S = {}
for i in range(N):
    S.update([(input(), 1)])
s = S.keys()
print(len(s))