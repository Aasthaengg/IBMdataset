def make_new_vocab(voc):
    max_let = ord(max(voc)) - 97
    let = [chr(ord('a') + i) for i in range(26)]

    for i in range(max_let + 2):
        yield voc + let[i]


n = int(input())
vocabs = ["a"]


for i in range(1, n):
    new_vocabs = []
    for voc in vocabs:
        for p in make_new_vocab(voc):
            new_vocabs.append(p)
    vocabs = new_vocabs

for ans in vocabs:
    print(ans)