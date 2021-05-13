a=''
while True:
    try:
        str = input().lower()
        a+=str
    except:
        break
for i in range(97, 97 + 26):
    count = 0
    for j in a:
        if chr(i) == j:
            count += 1
    print(chr(i), ':', count)
