T = raw_input()
wordList = []

W = raw_input()
while(W!="END_OF_TEXT"):
    wordList.extend(W.split(" "))
    W = raw_input()

cnt = 0
for word in wordList:
    if(word.lower() == T.lower()):
        cnt += 1
print cnt