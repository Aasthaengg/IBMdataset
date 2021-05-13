count_char = list(0 for i in range(26))
while True :
    try :
        str_org = str(input())
        str_org = str_org.lower()
        for i in range(len(str_org)) :
            num_org = ord(str_org[i])
            if num_org > 96 and num_org < 123 :
                count_char[num_org - 97] += 1
    except EOFError :
        break
for i in range(97, 123) :
    print(chr(i), ":", count_char[i-97])
