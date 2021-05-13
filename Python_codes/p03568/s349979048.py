n = int(input())
a = [int(x) for x in input().split()]
odds = len([1 for x in a if x % 2 == 0])

ans = 3**n - 2**odds
print(ans)