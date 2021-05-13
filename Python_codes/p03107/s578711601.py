S = list(input())
A = 0
B = 0
for s in S:
    if s == '0':
        A += 1
    else:
        B += 1
print(min(A,B)*2)