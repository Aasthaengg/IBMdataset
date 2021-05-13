def prime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
a=int(input())
for i in range(a, 100004):
    if prime(i):
        print(i)
        break