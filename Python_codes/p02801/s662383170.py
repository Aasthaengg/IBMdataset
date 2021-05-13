s = input()
list_s = list(range(97, 97+26))
for i in range(26):
    if ord(s) == list_s[i]:
        print(chr(list_s[i+1]))