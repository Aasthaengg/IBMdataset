s = input()
 
first_A = None
last_Z = None
for i, c in enumerate(s):
    if c == 'A' and first_A is None:
        first_A = i
    if c == 'Z':
        last_Z = i
 
print(last_Z-first_A+1)