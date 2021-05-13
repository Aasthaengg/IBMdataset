n = int(input())
bluedict = {}
for i in range(n):
    word = input()
    if bluedict.get(word) == None:
        bluedict[word] = 1
    else:
        bluedict[word] += 1

m = int(input())
reddict = {}
for i in range(m):
    word = input()
    if reddict.get(word) == None:
        reddict[word] = 1
    else:
        reddict[word] += 1

m = 0
for blueword in bluedict.keys():
    c = 0
    c += bluedict[blueword]
    if reddict.get(blueword) != None:
        c -= reddict[blueword]
    m = max(m,c)

print(m)