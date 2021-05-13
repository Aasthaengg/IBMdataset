N = int(input())
array1 = list(map(int,input().split()))
array2 = list(map(int,input().split()))
ma = 0
for i in range(N):
    candy = sum(array1[:i+1])+sum(array2[i:])
    ma = max(ma,candy)
print(ma)