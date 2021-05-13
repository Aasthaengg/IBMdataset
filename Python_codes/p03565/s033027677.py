s = input()
t = input()
import sys
revs = list(reversed(s))
revt = list(reversed(t))
if len(s) < len(t):
    print("UNRESTORABLE")
else:
    cur = 0
    for _ in range(len(s)-len(t)+1):
        char = revs[cur:cur+len(t)]
        charcopy = char.copy()
        for i,c in enumerate(char):
            if (i == len(char)-1) & ((c == "?") | (c == revt[i])):
                revs[cur:cur+len(t)] = revt
                for j in range(len(revs)):
                    if revs[j] == "?":
                        revs[j] = "a"
                print("".join(list(reversed(revs))))
                sys.exit()
            elif (c == "?") | (c == revt[i]):
                char[i] == revt[i]
            else:
                cur += 1
                break
        else:
            char = charcopy      
    else:
        print("UNRESTORABLE")