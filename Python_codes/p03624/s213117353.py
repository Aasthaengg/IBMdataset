s=input()
for i in range(26):
    if not chr(97+i) in s:
        print(chr(97+i))
        exit()
print("None")