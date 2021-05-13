S = input()
count = 0
val = 0

if len(S) % 2 == 0:
    val = len(S)/2
else:
    val = (len(S)-1)/2

for i in range(len(S)):
    if S[i] != S[-i-1]:
        count += 1
    if i+1 == val:
        break

print(count)
