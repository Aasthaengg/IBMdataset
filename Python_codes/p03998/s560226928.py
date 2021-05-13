Sa = input()
Sb = input()
Sc = input()

x = 'a'

while True:
    if x == 'a':
        if len(Sa) == 0:
            print('A')
            break
        x = Sa[0]
        Sa = Sa[1:len(Sa)]
    elif x == 'b':
        if len(Sb) == 0:
            print('B')
            break
        x = Sb[0]
        Sb = Sb[1:len(Sb)]
    elif x == 'c':
        if len(Sc) == 0:
            print('C')
            break
        x = Sc[0]
        Sc = Sc[1:len(Sc)]