a,b,c,d = map(int,input().split())

th1 = "R"*(c-a)
th2 = "U"*(d-b)
th3 = "L"*(c-a)
th4 = "D"*(d-b)
th5 = "D"+"R"*(c-a+1)+"U"*(d-b+1)+"L"
th6 = "U"+"L"*(c-a+1)+"D"*(d-b+1)+"R"

ans=th1+th2+th3+th4+th5+th6
print(ans)