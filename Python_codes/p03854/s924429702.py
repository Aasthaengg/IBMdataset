S = input()
while len(S)>0:
    if S[-7:] == "dreamer":
        S = S[:-7]
    elif S[-6:] == "eraser":
        S = S[:-6]
    elif S[-5:] == "dream":
        S = S[:-5]
    elif S[-5:] == "erase":
        S = S[:-5]
    else:
        break
print("YES" if len(S)==0 else "NO")