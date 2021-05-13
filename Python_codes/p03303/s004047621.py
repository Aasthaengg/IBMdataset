S = input()
w = int(input())
L = []
for i in range(len(S)):
        if i%w == 0:
                L.append(S[i])
print("".join(L))