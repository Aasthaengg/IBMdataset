N=int(input())

result=0
for i in range(1,N+1):
    if i%2!=0:
        divisor=0
        for j in range(1,i+1):
            if i%j==0:
                divisor+=1
        if divisor==8:
            result+=1
print(result)