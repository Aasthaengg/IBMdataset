n = input()
digit = len(n) - 1
if n.count('9') == len(n):
    print(9*len(n))
else:
    if digit > 0:
        if n[1:].count('9') == len(n[1:]):
            print(9*digit + int(n[0]))
        else:
            print(9*digit + int(n[0])-1)
    else:
        print(n[0])