S = input()
a = len(S)
b = -1
for i in range(len(S)):
    if S[i] == "C":
        a = i
        break
for i in range(len(S)):
    if S[len(S)-i-1] == "F":
        b = len(S)-i-1
        break
if a < b:
    print("Yes")
else:
    print("No")