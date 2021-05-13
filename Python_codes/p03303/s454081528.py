S = input()
w = int(input())
O = []

i = 0
while i < len(S):
    O.append(S[i])
    i += w

print("".join(O))