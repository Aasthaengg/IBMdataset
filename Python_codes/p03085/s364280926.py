S=input()
ans=""
for s in S:
    if s=="A":
        ans+="T"
    elif s=="T":
        ans+="A"
    elif s=="C":
        ans+="G"
    else:
        ans+="C"
print(ans)
