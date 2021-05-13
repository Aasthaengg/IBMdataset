leftp,rightp=0,0
loopnum = int(input())

for i in range(loopnum):
    st=input().split()
    stnew = sorted(st)
        
    if st[0]==st[1]:
        leftp = leftp+1
        rightp = rightp+1
    elif st != stnew:
        leftp=leftp+3
    elif st == stnew:
        rightp = rightp+3
        
print(str(leftp)+" "+str(rightp))
