k, t = map(int, input().split())
a = list(map(int, input().split()))

maxi = max(a)
wa = sum(a)
print(max(0, maxi-1-(wa-maxi)))