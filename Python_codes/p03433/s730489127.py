N = int(input())
A = int(input())

ans = 0


while ans<=(N-500):
    ans += 500

if (ans+A)>=N:
    print('Yes')
else:
    print('No')



