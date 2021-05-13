s = input()
n = len(s)
sw = 0
if "C" in s:
    a = s.index("C")
    if "F" in s:
        b = s[::-1].index("F")
        b = n-1 - b
        if a < b:
            sw = 1
            
print(["No","Yes"][sw])