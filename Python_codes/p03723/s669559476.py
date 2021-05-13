A,B,C = map(int, input().split())
A_first,B_first,C_first = A,B,C

result = 0
for i in range(10**9):
    if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
        break
    a = A // 2
    b = B // 2
    c = C // 2
    A = b + c
    B = a + c
    C = a + b
    if A == A_first and B == B_first and C == C_first:
        result = -1
        break
    result += 1   
print(result)    