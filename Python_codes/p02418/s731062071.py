cir = (str(input()))
cir_l = list(cir)
a = list(cir)
word = str(input())
word_l = list(word)
c = 0
for i in range(len(a)):
    cir_l.append(a[i])
for i in range(len(a)):
    w = ''
    for k in range(len(word_l)):
        w = w + cir_l[i+k]
    if (w == word):
        c = 1
if (c):
    print('Yes')
else:
    print('No')
    
