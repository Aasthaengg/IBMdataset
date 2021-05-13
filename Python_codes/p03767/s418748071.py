n = int(input())
arr = list(map(int, input().split()))
arr.sort()
arr = arr[n:]
arr2 = [arr[i] for i in range(len(arr)) if i % 2 == 0]
ans = sum(arr2)
print(ans)