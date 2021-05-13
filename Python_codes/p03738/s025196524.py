A = input()
B = input()

LA = len(A)
LB = len(B)

if LA > LB:
    ans = 'GREATER'
elif LA < LB:
    ans = 'LESS'
else:
    for a, b in zip(A, B):
        if a > b:
            ans = 'GREATER'
            break
        elif a < b:
            ans = 'LESS'
            break
    else:
        ans = 'EQUAL'

print(ans)
