S = input()[::-1]
word1 = "dream"[::-1]
word2 = "dreamer"[::-1]
word3 = "erase"[::-1]
word4 = "eraser"[::-1]
while True:
    if S[:5] == word1:
        S = S[5:]
    elif S[:7] == word2:
        S = S[7:]
    elif S[:5] == word3:
        S = S[5:]
    elif S[:6] == word4:
        S = S[6:]
    elif S == "":
        print("YES")
        break
    else:
        print("NO")
        break
