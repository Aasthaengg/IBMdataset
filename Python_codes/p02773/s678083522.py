n = int(input())
d = {}
for i in range(n):
    S = input()
    d[S] = d[S]+1 if S in d else 1
L = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(*sorted([l[0] for l in L if l[1] == L[0][1]]), sep='\n')