s=input()
ans="WA"
if s[0]=="A":
    if s[2:-1].count("C")==1:
        s=list(s)
        s.remove("A")
        s.remove("C")
        for j in range(len(s)):
            if ord(s[j])<ord("a"):
                break
        else:
            ans="AC"
print(ans)