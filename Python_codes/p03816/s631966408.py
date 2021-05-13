N = int(input())
arr = list(map(int, input().split()))
print(N-(-(-(N-len(set(arr)))//2))*2)
