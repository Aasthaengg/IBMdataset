z=''
while True:
    try:
        z += input()
    except EOFError:
        break
a = []
b = 0
for i in z:
    if i.isupper():
        a += i.lower()
    a += i
al = [chr(i) for i in range(97, 97 + 26)]
for i in al:
    b = str(a.count(i))
    print('{} : {}'.format(i,b))