N=int(input())
K=int(input())
number=1
for _ in range(N):
    if number*2>number+K:
        number=number+K
    else:
        number=number*2
print(number)
