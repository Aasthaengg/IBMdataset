import copy
SD = list(input())
T = list(input())

Possible = []
for TSD in range(0,len(SD)-len(T)+1):
    SDCopy = copy.deepcopy(SD)
    String = SDCopy[TSD:TSD+len(T)]
    Flag = True
    for TST in range(0,len(T)):
        if String[TST]!='?' and String[TST]!=T[TST]:
            Flag = False
            break
    if Flag:
        SDCopy[TSD:TSD+len(T)] = T
        Possible.append(''.join(['a' if TSC=='?' else TSC for TSC in SDCopy]))
if Possible:
    print(sorted(Possible)[0])
else:
    print('UNRESTORABLE')