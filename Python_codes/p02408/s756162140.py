n=input()
S=[range(1,14) for j in range(4)]
for i in range(n):
    ip=raw_input().split()
    if ip[0]=='S':
        S[0].remove(int(ip[1]))
    elif ip[0]=='H':
        S[1].remove(int(ip[1]))
    elif ip[0]=='C':
        S[2].remove(int(ip[1]))
    else :
        S[3].remove(int(ip[1]))
for i in S[0]:
   print 'S '+str(i)
for i in S[1]:
   print 'H '+str(i)
for i in S[2]:
   print 'C '+str(i)
for i in S[3]:
   print 'D '+str(i)