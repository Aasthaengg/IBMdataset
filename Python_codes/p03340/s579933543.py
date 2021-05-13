N = int(input())
num = list(map(int, input().split()))

xorsum = 0
sumz = 0
totallen = 0#N
right = 0
for left in range(N):
    while right < N and (sumz + num[right]) == (xorsum ^ num[right]):
        sumz += num[right]
        xorsum ^= num[right]
        right += 1

    totallen += (right - left)
    if right <= left:
        right += 1
    else:
        sumz -= num[left]
        xorsum ^= num[left]

print(totallen)

