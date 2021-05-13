S=input()
F=["dream","dreamer","erase","eraser"]

B=""
while B!=S:
    B=S
    for X in F:
        a=len(X)
        if S[-a:]==X:
            S=S[:-a]

if S:
    print("NO")
else:
    print("YES")