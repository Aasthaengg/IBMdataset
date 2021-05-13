S = input()
w = int(input())

newS =[""]
i = 0

while i<len(S):
    newS.append(S[i])
    i = i+w

print("".join(newS))