A = list(input())
B = list(input())
result = 'EQUAL'
if len(A) > len(B):
    result = 'GREATER'
elif len(B) > len(A):
    result = 'LESS'
else:
    for i in range(len(A)):
        if A[i] > B[i]:
            result ='GREATER'
            break
        elif B[i] > A[i]:
            result = 'LESS'
            break
print(result)    