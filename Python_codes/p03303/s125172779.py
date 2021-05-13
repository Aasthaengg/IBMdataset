S = input()
w = int(input())

newS = [""] * ((len(S) - 1 + w) // w)

for i in range(len(newS)):
    newS[i] = S[w * i]

print("".join(newS))
