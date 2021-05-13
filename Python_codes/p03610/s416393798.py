S = input()
s = []
for i in range(len(S)):
    if i % 2==0:
        s.append(S[i])
print("".join(map(str,s)))