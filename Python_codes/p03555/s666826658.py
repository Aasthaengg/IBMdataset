C = ""
for i in range(2):
    C += input()
    
if list(C) == list(reversed(C)):
    print("YES")
else:
    print("NO")