def find_card(mark,input,result):
    for i in xrange(13):
        if input[i] == 0:
            result.append(i)
    result.sort()
    for x in result:
        print mark + " " +  str(x+1)

n = input()
s = [0]*13
h = [0]*13
c = [0]*13
d = [0]*13
for i in xrange(n):
    m,n = map(str,raw_input().split())
    n = int(n)-1
    if m in "S" :
        s[n] = 1
    elif m in "H":
        h[n] = 1
    elif m in "C":
        c[n] = 1
    elif m in "D":
        d[n] = 1

res_s=[]
res_h=[]
res_c=[]
res_d=[]

find_card("S",s,res_s)
find_card("H",h,res_h)
find_card("C",c,res_c)
find_card("D",d,res_d)