from sys import stdin
S = (stdin.readline().rstrip())
flag = False
for i in ["","A"]:
    for j in ["","A"]:
        for k in ["","A"]:
            for l in ["","A"]:
                s = i + "KIH" + j + "B" + k + "R" + l
                if S == s:
                    flag = True
if flag:
    print("YES")
else:
    print("NO")