S = input()

while 1:
    for target in ["dream", "dreamer", "erase", "eraser"]:
        if S.endswith(target):
            S = S[:-len(target)]
            break
    else:
        print("NO")
        break
    if len(S) == 0:
        print("YES")
        break