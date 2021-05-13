x,y,a,b=map(int,input().split())
a=a-x ; b=b-y 

ans="R"*a + "U"*b + "L"*a + "D"*(b+1) + "R"*(a+1) + "U"*(b+1) + "L"
ans+="U" + "L"*(a+1) + "D"*(b+1) + "R"
print(ans) 

