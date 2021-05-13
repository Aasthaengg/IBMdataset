S = list(input().strip())

w_count = 0
move = 0
for i in range(len(S)-1,-1,-1):
    if S[i] == "B":
        move += w_count
    else:
        w_count += 1

print(move)