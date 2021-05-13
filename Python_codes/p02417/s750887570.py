alphabet = [0 for i in range(26)]

while True:
    try:
        word = input()
    except:
        break
    word_s=str.lower(word)
    for i in range(len(word_s)):
        a = ord(word_s[i])-ord('a')
        if (a >= 0 and a < 26):
            alphabet[a]+=1
        
for i in range(26):
    print(chr(i+ord('a')),":",alphabet[i])
