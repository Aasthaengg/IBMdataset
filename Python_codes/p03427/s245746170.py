n = str(input())

o = len(n)-1

if o == 0:
    print(n)
elif n[1:] == "9" * o:
    print(int(n[0]) + 9*o)
else:
    print(int(n[0]) - 1 + 9*o)