N = int(input())
A = list(map(int,input().split()))
suma = 0
left = 0
right = 0
count = 0
while left != N:
    if right == N:
        count += right-left
        suma -= A[left]
        left += 1
    elif suma+A[right] == suma^A[right]:
        suma += A[right]
        right += 1
    else:
        count += right - left
        suma -= A[left]
        left += 1
print(count)