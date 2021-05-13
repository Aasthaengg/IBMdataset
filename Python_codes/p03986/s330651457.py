s = input()
cur = 0
deletedpairs = 0
for i in range(len(s)):
    #print(i, deletedpairs)
    if s[i] == "S":
        cur += 1
    if s[i] == "T":
        if cur > 0:
            deletedpairs += 1
            cur -= 1
        else:
            pass

#print(deletedpairs)
print(len(s) - deletedpairs*2)