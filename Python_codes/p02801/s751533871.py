c = input()
l = [chr(i)for i in range(97,97+26)]

if c in l:
    print(l[ord(c)+1-97])

else:
    pass