a, b, c, d = map(int,input())
A = str(a)
B = str(b)
C = str(c)
D = str(d)
if a+b+c+d == 7:
    print(A+'+'+B+'+'+C+'+'+D+'=7')
elif a-b+c+d == 7:
    print(A+'-'+B+'+'+C+'+'+D+'=7')
elif a+b-c+d == 7:
    print(A+'+'+B+'-'+C+'+'+D+'=7')
elif a+b+c-d == 7:
    print(A+'+'+B+'+'+C+'-'+D+'=7')
elif a-b-c+d == 7:
    print(A+'-'+B+'-'+C+'+'+D+'=7')
elif a-b+c-d == 7:
    print(A+'-'+B+'+'+C+'-'+D+'=7')
elif a+b-c-d == 7:
    print(A+'+'+B+'-'+C+'-'+D+'=7')
elif a-b-c-d == 7:
    print(A+'-'+B+'-'+C+'-'+D+'=7')