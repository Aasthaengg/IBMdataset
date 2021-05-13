A = int(input())
x = list(map(int, input().split()))

kotae='APPROVED'
for i in range(len(x)):
    if x[i]%2==0:
        if x[i]%3==0 or x[i]%5==0:
            pass
        else:
            kotae='DENIED'


print(kotae)
