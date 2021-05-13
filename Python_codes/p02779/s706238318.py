n = int(input())
arr = list(map(int, input().split()))
arr = set(arr)
print("YES" if len(arr) == n else "NO")