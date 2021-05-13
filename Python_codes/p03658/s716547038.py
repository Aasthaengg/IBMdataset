N,K = map(int,input().split())
array = list(map(int,input().split()))
array.sort(reverse=True)
result = 0
for i in range(K):
    result += array[i]
print(result)