S = input()
sl = []
for i in range(len(S)):
    sl.append(S[i])
count = 0
memo = 0
for i in range(len(S)-1):
    if sl[i] == "B" and sl[i+1] == "W":
        count += 1+memo
        sl[i+1] = "B"
    elif sl[i] == "B" and sl[i+1] == "B":
        memo += 1

print(count)
