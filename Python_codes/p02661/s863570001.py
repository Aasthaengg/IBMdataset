N = int(input())
array1 = []
array2 = []
for i in range(N):
    a,b = map(int,input().split())
    array1.append(a)
    array2.append(b)

array1.sort()
array2.sort()

if N % 2 == 0:
    min = array1[N//2]+array1[N//2-1]
    max = array2[N//2]+array2[N//2-1]
    print(max-min+1)
else:
    min = array1[N//2]
    max = array2[N//2]
    print(max-min+1)
