#-*- coding:utf-8 -*-
#approach:
#????????????????????±??????N???S??????????????¨W???E??????????????¨????????????
rolls = raw_input().split()
order = raw_input().strip()
nsrolls = [rolls[0],rolls[1],rolls[5],rolls[4]]
werolls = [rolls[0],rolls[2],rolls[5],rolls[3]]
while True:
    if order == "":
        break
    o = order[0]
    if o=="N":
        tmp = nsrolls[0]
        nsrolls.pop(0)
        nsrolls.append(tmp)
        werolls[0]=nsrolls[0]
        werolls[2]=nsrolls[2]
    elif o=="S":
        tmp = nsrolls[-1]
        nsrolls.pop(-1)
        nsrolls.insert(0,tmp)
        werolls[0]=nsrolls[0]
        werolls[2]=nsrolls[2]
    elif o=="W":
        tmp = werolls[0]
        werolls.pop(0)
        werolls.append(tmp)
        nsrolls[0]=werolls[0]
        nsrolls[2]=werolls[2]
    elif o=="E":
        tmp = werolls[-1]
        werolls.pop(-1)
        werolls.insert(0,tmp)
        nsrolls[0]=werolls[0]
        nsrolls[2]=werolls[2]
    else:
        print "invalid order"
    order = order[1:]
print nsrolls[0]