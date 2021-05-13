s=input()

if(len(s) == 2):
    print(s)
else:
    for ch in s[::-1]:
        print(ch, end='')