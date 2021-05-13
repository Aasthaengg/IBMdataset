s = input()

if s[1:].count("9") == len(s)-1:
    print(9*(len(s)-1)+int(s[0]))
else:
    print(9*(len(s)-1)+int(s[0])-1)