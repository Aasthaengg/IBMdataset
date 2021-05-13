string = str(input())
for c in string:
    if c.isupper():
        print(c.lower(),end='')
    elif c.islower():
        print(c.upper(),end ='')
    else:
        print(c,end ='')
print('')