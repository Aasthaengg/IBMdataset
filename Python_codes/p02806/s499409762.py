N = int(input())
S = []
T = []
for i in range(N):
    s,t = input().split()
    S.append(s)
    T.append(int(t))

X = str(input())
ind = int(S.index(X))
print(sum(T[ind+1:]))