N,A,B = map(int,input().split())
l = 0
num = 0
Sum = 0
for i in range(1,N+1):
    i = str(i)
    l = len(i)
    for j in range(l):
        num += int(i[j])
    if A<=num and B >= num:
        Sum += int(i)
    num = 0
print(Sum)