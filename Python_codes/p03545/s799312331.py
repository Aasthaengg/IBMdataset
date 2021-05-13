n=input()
l=len(n)-1
s=[n[0]]
for i in range(2**l):
    x=['-']*l
    for j in range(l):
          if ((i >> j) & 1):
              x[l - 1 - j]='+'
    for i in range(l):
        s.append(x[i])
        s.append(n[i+1])
    if eval(''.join(s))==7:
        s+='=7'
        print(''.join(s))
        exit()
    s=[n[0]]