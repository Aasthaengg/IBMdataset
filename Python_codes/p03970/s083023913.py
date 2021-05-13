A = str('CODEFESTIVAL2016')
B = str(input())
ans = 0
for i in range(16):
    if A[i] != B[i]:
        ans += 1
        
print(ans)