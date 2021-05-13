b = input()
AC = ["A", "C"]
GT = ["G", "T"]

if b in AC:
    b = GT[b == "A"]
    
elif b in GT:
    b = AC[b == "G"]
    
print(b)