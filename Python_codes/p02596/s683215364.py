K = int(input())
i = 1

if K % 5 == 0 or K % 2 == 0:
    i = -1
N = 0
while True:
    if i == -1:
        break
    N = (N * 10 + 7)  %K 
    if N % K != 0:
        i += 1
    else:
        break
print(i)