import itertools

N = int(input())
MARCH=[0]*5
ans = 0
for _ in range(N):
    S = (input())[0]
    if S == 'M':
        MARCH[0]+=1
    if S == 'A':
        MARCH[1]+=1
    if S == 'R':
        MARCH[2]+=1
    if S == 'C':
        MARCH[3]+=1
    if S == 'H':
        MARCH[4]+=1

C =  itertools.combinations(MARCH, 3)
for c in C:
    ans += c[0]*c[1]*c[2]

print(ans)
