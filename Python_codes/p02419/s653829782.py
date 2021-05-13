findstr = raw_input().strip()
findstr = findstr.lower()
inlist = []
while True:
    tmplist = (raw_input().replace("\r"," ")).split()
    # print tmplist
    if tmplist[0] == "END_OF_TEXT":
        break
    inlist.extend(tmplist)
count = 0
for i in xrange(len(inlist)):
    if inlist[i].lower() == findstr.lower():
        count+=1
print count