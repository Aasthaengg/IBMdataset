alphabets = [chr(i) for i in range(97,123)]  #list into alphabets
cnt = input()
if cnt in alphabets:
    x = alphabets.index(cnt)+1
    print(alphabets[x])