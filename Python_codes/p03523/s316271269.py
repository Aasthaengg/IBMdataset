from re import fullmatch

S=input()
print("YES" if fullmatch("A?KIHA?BA?RA?",S) else "NO")
