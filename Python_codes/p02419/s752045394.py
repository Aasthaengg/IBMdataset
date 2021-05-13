w = input()
small = 'abcdefghijklmnopqrstuvwxyz'
large = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
count = 0
while True:
    text = input()
    if text == 'END_OF_TEXT':
        break
    else:
        stext = ''
        for i in text:
            j = 0
            while j < 26:
                if i == large[j]:
                    stext += small[j]
                    break
                j += 1
            if j == 26:
                stext += i
        t = list(map(str, stext.split(' ')))
        for p in t:
            if p == w:
                count += 1
print(count)
