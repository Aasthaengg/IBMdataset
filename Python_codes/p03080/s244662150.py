N = int(input())
S = input()

r=0
b=0

for n in range(N):
    if S[n] == 'R':
        r +=1
    if S[n] == 'B':
        b +=1

if r>b:
    print('Yes')
else:
    print('No')