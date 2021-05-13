X = list(input())
N = len(X)
Life = 0
out = 0
for i in range(N):
    if X[i]=="S":
        Life += 1
    elif X[i]=="T":
        if Life==0:
            out += 1
        elif Life>0:
            Life += -1
print(out+Life)
