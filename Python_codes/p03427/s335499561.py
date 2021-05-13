s = input()
cnt = len(s)

if s[0] == "9":
    if s[1:] == "9"*(cnt-1):
        print(9*cnt)
    else:
        print(8+9*(cnt-1))
else:
    if s[1:] == "9"*(cnt-1):
        print(int(s[0]) + 9*(cnt-1))
    else:
        print((int(s[0])-1) + 9*(cnt-1))