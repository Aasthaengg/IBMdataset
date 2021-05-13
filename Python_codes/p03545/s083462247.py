s = input()
a = s[0]
b = s[1]
c = s[2]
d = s[3]
op = ['+','-']

for v in op:
    for w in op:
        for x in op:
            l = str(a+v+b+w+c+x+d)
            if eval (l) == 7:
                print (l+"=7")
                exit ()
