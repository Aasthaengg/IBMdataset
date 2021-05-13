n = int(input())
a_li = list(map(int,input().split()))
dum1 = a_li[0::2]
dum2 = a_li[1::2]
if n%2 == 0:
    dum2 = dum2[::-1]
    dum1 = " ".join(map(str,dum1))
    dum2 = " ".join(map(str,dum2))
    print(dum2+" "+dum1)
else:
    dum1 = dum1[::-1]
    dum1 = " ".join(map(str,dum1))
    dum2 = " ".join(map(str,dum2))
    print(dum1+" "+dum2)
