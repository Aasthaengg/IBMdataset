A = input()
B = input()
if len(A) > len(B):
    ans = 'GREATER'
elif len(A) < len(B):
    ans = 'LESS'
elif len(A) == len(B):
    ans = 'EQUAL'
    for i in range(len(A)):
        if int(A[i]) > int(B[i]):
            ans = 'GREATER'
            break
        elif int(A[i]) < int(B[i]):
            ans = 'LESS'
            break
print(ans)