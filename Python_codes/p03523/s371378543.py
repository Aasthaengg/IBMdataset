import sys
s = [c for c in "AKIHABARA"]
L = []
for i in range(0, 2):
    for j in range(0, 2):
        for k in range(0, 2):
            for l in range(0, 2):
                if i == 0:
                    s[0] = "X"
                if j == 0:
                    s[4] = "X"
                if k == 0:
                    s[6] = "X"
                if l == 0:
                    s[8] = "X"
                while "X" in s:
                    s.remove("X")
                L.append(s)
                s = [c for c in "AKIHABARA"] #bitで書きたかった・・・。
S = [c for c in input()]
for el in L:
    if S == el:
        print("YES")
        sys.exit(0)
print("NO")