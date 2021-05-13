s = str(input())
s = s[:-1]
half = len(s)//2
#print(half)
while s[:half] != s[half:]:
    s = s[:-1]
    half = len(s)//2
    
print(len(s))    