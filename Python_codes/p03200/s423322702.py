S = list(input())
c = 0
w = 0
for i in range(len(S)) :
    if S[i] == 'W' :
        c += i - w
        w += 1
print(c)