sum=0
minb=10
for i in range(5):
    a=int(input())
    sum += a//10*10 if a%10==0 else a//10*10+10
    b = a%10
    minb = min(minb if b==0 else b, minb)
print(sum-10+minb)

