s=input()

if s[:1]=="k" and s[len(s)-6:]=="eyence":
    print("YES")
elif s[:2]=="ke" and s[len(s)-5:]=="yence":
    print("YES")
elif s[:3]=="key" and s[len(s)-4:]=="ence":
    print("YES")
elif s[:4]=="keye" and s[len(s)-3:]=="nce":
    print("YES")
elif s[:5]=="keyen" and s[len(s)-2:]=="ce":
    print("YES")
elif s[:6]=="keyenc" and s[len(s)-1:]=="e":
    print("YES")
elif s[:7]=="keyence":
    print("YES")
elif s[len(s)-7:]=="keyence":
    print("YES")
else:
    print("NO")