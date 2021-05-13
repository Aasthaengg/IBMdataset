N = int(input())
A = [int(n) for n in input().split() if int(n)%2==0]
c = 0
for a in A:
    if a%3==0 or a%5==0:
        c += 1
print('APPROVED' if c==len(A) else 'DENIED')
