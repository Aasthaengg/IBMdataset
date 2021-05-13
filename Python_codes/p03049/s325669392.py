
N = int(input())
AB = 0
A = 0
B = 0
BA = 0
for i in range(N):
    s = list(input())
    for i in range(len(s)-1):
        if s[i] == 'A' and s[i+1] == 'B':
            AB += 1
    if s[-1] == 'A' and s[0] == 'B':
        BA += 1
    elif s[-1] == 'A':
        A += 1
    elif s[0] == 'B':
        B += 1
if BA == 0:
    AB += min(A,B)
elif A+B > 0:
    AB += BA + min(A,B)
else:
    AB += BA-1
print(AB)
