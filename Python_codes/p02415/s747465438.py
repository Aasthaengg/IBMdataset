def changeUL(str):
    if(str.islower()):
        return str.upper()
    else:
        return str.lower()
rc=list(map(changeUL,list(input())))
print("".join(rc))