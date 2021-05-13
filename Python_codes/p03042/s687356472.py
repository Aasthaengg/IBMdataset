s = input()

n1 = s[0:2]
n2 = s[2:4]

if int(n1) > 12 and int(n2) > 12:
    out_print = 'NA'

elif int(n1) <= 12 and int(n2) <= 12:
    out_print = 'AMBIGUOUS'
    if int(n1) == 0 and int(n2)!=0:
        out_print = 'YYMM'
    elif int(n1) != 0 and int(n2) == 0:
        out_print = 'MMYY'
    elif int(n1)==0 and int(n2)==0:
        out_print = 'NA'

elif int(n1) <= 12 and int(n2) >12:
    out_print = 'MMYY'
    if int(n1) == 0:
        out_print = 'NA'

elif int(n1) > 12 and int(n2) <= 12:
    out_print = 'YYMM'
    if int(n2) == 0:
        out_print = 'NA'
print(out_print)
