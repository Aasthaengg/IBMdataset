b = [0]*26
while True:
    try: 
        a = raw_input()
        for i in a:
            c = ord(i.lower())
            if c>= ord("a") and c <= ord("z"):
                b[c-ord("a")] +=1
    except EOFError,e:
        break
for i,v in enumerate(b):
    print "{0} : {1}".format(chr(i+ord("a")),v)