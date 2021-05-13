N = int(input())
prime = [True] * 55556
prime[0] = False
prime[1] = False
for i in range(4,55556,2):
    prime[i] = False
for i in range(3,55556,2):
    if prime[i] == True:
        for j in range(i*2,55556,i):
            prime[j] = False
lis = []
for i in range(55556):
    if prime[i] == True and i % 5 == 1:
        lis.append(i)
    if len(lis) == N:
        break

print(' '.join(map(str,lis)))
