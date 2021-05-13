def resolve():
    s = input()
    al = []
    for i in range(26):
        al.append(False)
    
    for c in s:
        ord_c = ord(c) - ord('a')
        al[ord_c] = True
    
    for i in range(26):
        if al[i] == False:
            print(chr(ord('a') + i))
            break
        if i == 25 and al[i] == True:
            print("None")
resolve()