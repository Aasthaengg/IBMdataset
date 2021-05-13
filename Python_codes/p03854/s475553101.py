S = input()

idx = len(S)
while idx > 0:
    if S[idx-7:idx] == "dreamer":
        idx -= 7
    elif S[idx-6:idx] == "eraser":
        idx -= 6
    elif S[idx-5:idx] in ["dream", "erase"]:
        idx -= 5
    else:
        print("NO")
        break
else:
    print("YES")