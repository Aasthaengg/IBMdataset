b = input()

def tog(s):
    if s=="A":
        return "T"
    elif s=="T":
        return "A"
    elif s=="C":
        return "G"
    elif s=="G":
        return "C"
    else:
        return None

print(tog(b))