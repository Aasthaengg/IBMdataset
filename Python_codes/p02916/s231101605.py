N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

t = 1000000000
lis = list()
for i in A:
    lis.append(B[i-1])
    #print(i,t)
    if i == t + 1:
        lis.append(C[i-2])
    t = i

print(sum(lis))