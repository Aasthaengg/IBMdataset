text = ""
while 1:
    try:
        x = input()
        text += x
    except EOFError:
        break
text_new = text.lower()
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in alphabet:
    tmp = 0
    for j in text_new:
        if j == i:
            tmp += 1
    print(i + " : " + str(tmp))

