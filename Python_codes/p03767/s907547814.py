n = int(input())
print(sum(sorted(list(map(int, input().split())))[n::2]))