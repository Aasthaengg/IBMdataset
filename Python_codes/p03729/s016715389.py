S_1, S_2, S_3 = map(str,input().split())
if S_1[-1] == S_2[0] and S_2[-1] == S_3[0] :
    result = "YES"
else :
    result = "NO"
print(result)