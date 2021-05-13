n = int(input())
list_A = list(map(int, input().split()))

ans = max(list_A)-min(list_A)
print(ans)