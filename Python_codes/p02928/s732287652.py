def answer(arr, k):
    _mod = (10**9+7)
    left = 0
    right = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                left += 1
            if arr[i] < arr[j]:
                right += 1
    
    left = (left * (k*(k+1))//2)
    right = (right * (k*(k-1))//2)
    return int((left+right)%_mod)
    
n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(answer(arr, k))
# print(answer2(arr, k))