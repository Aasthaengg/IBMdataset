string = input()
for i, s in enumerate(string):
    if s == "A":
        start = i
        break
    
l = len(string)
for i, s in enumerate(string[::-1]):
    if s == "Z":
        end = l - i
        break
print(end - start)