s=input()
ls = len(s)
k= int(input())
for i in range(ls-1):
    tn = ord('z')-ord(s[i])+1
    if k>=tn and s[i]!='a':
        k-=tn
        print('a',end='')
    else:
        print(s[i],end='')
ik = (k + ord(s[-1])-ord('a')) % 26
print(chr(ord('a')+ik))