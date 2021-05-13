N,A,B=input().split()

sum=0
for i in range(int(N)+1):
    nums = list(str(i))
    tmp = 0
    for j in nums:
        tmp = tmp + int(j)
    if int(A)<=tmp:
        if tmp<=int(B):
            sum = sum + i
print(sum)
