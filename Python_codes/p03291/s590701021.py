mod = 10**9+7
S = input()
A = 0
AB = 0
ABC = 0

N = 1
for i in range(len(S)):
    if S[i] == 'A':
        A += N
    elif S[i] == 'B':
        AB += A
    elif S[i] == 'C':
        ABC += AB
    else:
        ABC = 3*ABC + AB
        AB = 3*AB + A 
        A = 3*A + N
        N *= 3
    A %= mod
    AB %= mod
    ABC %= mod
    N %= mod

print(ABC)