N = int(input())
ans = 0
for cake in range(N+1):
    for donut in range(N+1):
        if 4*cake + 7*donut == N:
            ans +=1
print('Yes' if ans>0 else 'No')