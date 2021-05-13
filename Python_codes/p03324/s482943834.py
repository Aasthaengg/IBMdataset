d,n = map(int,input().split())
case = 100**d
if n < 100:
    print(case*n)
else:
    print(101*case)