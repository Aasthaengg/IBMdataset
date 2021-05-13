first = str(input())
second = str(input())
"""
def cycleis(start, dici, seen):
    curr = start
    #print("Curr: {}".format(curr))
    while seen[curr] != 1:
        #print("Bent Curr: {}".format(curr))
        seen[curr] = 1
        curr = dici[curr]
        if curr not in seen:
            return True

    if curr == start:
        return True
    else:
        return False
"""
good = True
dici = {}
dici2 = {}
seen = {}
#Check if the same thing goes to the same 
for i in range(0,len(first)):
    if first[i] in dici:
        if second[i] != dici[first[i]]:
            print("No",end='')
            good = False
            #print("A hiba: {} -> {}-ba megy itt meg {}-be kene".format(first[i], dici[i], second[i]))
            break
    else:
        dici[first[i]] = second[i]

    if second[i] in dici2:
        if first[i] != dici2[second[i]]:
            print("No", end='')
            good = False
            break
    else:
        dici2[second[i]] = first[i]

    #if first[i] not in seen:
    #    seen[first[i]] = 0

#print("Seen: {}, Dici: {}".format(seen,dici))
#Final check if a->c->a if c was in first.
"""
for i in dici.keys():
    if cycleis(i, dici, seen) == False:
        print("No", end='')
        good = False
        break"""
"""
for i in dici.keys():
    if dici[i] in dici:
        if dici[dici[i]] != i:
            print("A hiba: {} -> {}-ba megy itt meg {}-be kene".format(i, dici[i], dici[dici[i]]))
            good = False
            print("No", end='')
            break
"""
if good:
    print("Yes",end='')
