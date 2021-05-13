n = int(input())
arr = list(map(int, input().split()))
arr.sort()
alice = 0
bob = 0
for i in range(len(arr)):
    if i%2 == 0:
        alice += arr[i]
    else:
        bob += arr[i]
print(abs(alice-bob))