S = raw_input()
T = ""
for x in S:
    if x.islower():
        T += x.upper()
    elif x.isupper():
        T += x.lower()
    else:
        T += x
print T