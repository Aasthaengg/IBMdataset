a=input()
while True:
    try:
        a+=(str(input()))
    except EOFError:
        break
b=str.lower(a)
for i in range(ord('a'),ord('z')+1):
    count=0
    print(chr(i),':',end=' ')
    for j in range(len(b)):
        c=ord(b[j])
        if i==c:
            count+=1
    print(count)
