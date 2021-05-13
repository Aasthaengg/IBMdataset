s = input()
q = int(input())
cou = 1
frt = ""
bck = ""
for i in range(q):
    t = list(input().split())
    #logging.debug(t)#
    if t[0] == "1":
        cou *= -1
    else:
        if (t[1] == "1" and cou == 1)or(t[1] == "2" and cou == -1):
            frt = t[2] + frt
        else:
            bck = bck + t[2]
#    logging.debug("s {},cou {}".format(s,cou))

s = frt + s + bck
#logging.debug(s)#
if cou == 1:
    print(''.join(s))
else:
    print(''.join(s[::-1]))