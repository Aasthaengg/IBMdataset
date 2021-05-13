A, B, X, Y = map(int, input().split())
P = X-A
Q = Y-B
print("R"*P+"U"*Q+"L"*P+"D"*Q+"L"+"U"*(Q+1)+"R"*(P+1)+"D"+\
"R"+"D"*(Q+1)+"L"*(P+1)+"U")