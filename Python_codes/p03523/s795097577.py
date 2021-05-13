S = input()
target = "AKIHABARA"
s = 0
for i in range(len(target)):
    if s < len(S):
        if S[s] != target[i]:
            if target[i] == "A":
                continue
            else:
                print("NO")
                break
        else:
            s += 1
    else:
        if target[i] == "A":
            continue
        else:
            print("NO")
            break
else:
    if s != len(S):
        print("NO")
    else:
        print("YES")
