s = input()
c = 'CODEFESTIVAL2016'
g = 0
for ss,cc in zip(s,c):
    if ss != cc:g+=1
print(g)