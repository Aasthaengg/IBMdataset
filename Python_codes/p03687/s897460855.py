S = input()
k = 1000 
for i in range (len(S)):
    x = y = 0
    for j in range (1, len(S) + 1):
        if S[i] == S[len(S)-j]:
            x = 0
        else:
            x += 1
        y = max(x,y)
    k = min(k,y)
print(k)