n = int(input())
A = list(map(int, input().split()))
can = True
count = 0

while(can):
    for i in range(len(A)):
        if(A[i] % 2 != 0):
            can = False
        else:
            A[i] = A[i] / 2
    if(can):
        count+=1
print(count)
