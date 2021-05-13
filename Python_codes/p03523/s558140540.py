S = str(input())

#AKIHABARA のAの有無で全パターン列挙
OK_word_set = set()

for i in range(2**(4)):
    bit_array = str(bin(i)[2:]).zfill((4))
    OK_word = ""

    #print(bit_array)

    if int(bit_array[0]) == 0:
        OK_word += "KI"
    elif int(bit_array[0]) == 1:
        OK_word += "AKI"
        
    if int(bit_array[1]) == 0:
        OK_word += "H"
    elif int(bit_array[1]) == 1:
        OK_word += "HA"
        
    if int(bit_array[2]) == 0:
        OK_word += "B"
    elif int(bit_array[2]) == 1:
        OK_word += "BA"
        
    if int(bit_array[3]) == 0:
        OK_word += "R"
    elif int(bit_array[3]) == 1:
        OK_word += "RA"

    #print(OK_word)   
    OK_word_set.add(OK_word)

#print(OK_word_set)

if S in OK_word_set:
    print("YES")
else:
    print("NO")