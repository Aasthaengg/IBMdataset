a,b,c,d=map(int,input().split())
a_b,c_d =a*b,c*d
if a_b==c_d:
    print(a_b)
else:
    print(max(a_b,c_d))