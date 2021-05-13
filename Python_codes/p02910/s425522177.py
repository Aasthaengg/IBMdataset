S=input()

if all(a!="L" for a in S[::2]) and all(a!="R" for a in S[1::2]):
    print("Yes")
else:
    print("No")
