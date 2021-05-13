s = input()
if s[0]=="A" and s[2:-1].count("C")==1:
    sc = s.index("C")
    if (s[1:sc]+s[sc+1:]).islower():
        print("AC")
    else:
        print("WA")
else:
    print("WA")