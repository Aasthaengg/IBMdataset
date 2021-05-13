N,A,B = map(int,input().split())

if A==B :
    if N == 1 :
        ans = "Borys"
    else :
        ans = "Alice"
else :
    if (B-A)% 2 == 0 :
        ans = "Alice"
    else :
        ans = "Borys"
print(ans)
