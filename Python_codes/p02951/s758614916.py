# A - Transfer


A, B, C = map(int, input().split())

# A madehairu B haitteru Ciretai

if A - B > C:
    answer = 0
else:
    answer = C - (A - B)

print(answer)

