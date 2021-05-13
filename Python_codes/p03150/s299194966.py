import re
s = input()
y = "YES"
n = "NO"
if s == "keyence":
    print(y)
elif re.fullmatch(r'[a-z]+keyence',s) != None:
    print(y)
elif re.fullmatch(r'k[a-z]+eyence',s) != None:
    print(y)
elif re.fullmatch(r'ke[a-z]+yence',s) != None:
    print(y)
elif re.fullmatch(r'key[a-z]+ence',s) != None:
    print(y)
elif re.fullmatch(r'keye[a-z]+nce',s) != None:
    print(y)
elif re.fullmatch(r'keyen[a-z]+ce',s) != None:
    print(y)
elif re.fullmatch(r'keyenc[a-z]+e',s) != None:
    print(y)
elif re.fullmatch(r'keyence[a-z]+',s) != None:
    print(y)
else:
    print(n)
