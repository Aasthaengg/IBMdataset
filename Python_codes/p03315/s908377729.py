S = input()
out = 0
for i in range(len(S)):
    if S[i]=="+":
        out += 1
    elif S[i]=="-":
        out += -1
print(out)
