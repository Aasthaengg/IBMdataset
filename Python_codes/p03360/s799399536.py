a, b, c = map(int, input().split())
k = int(input())
rem = sum((a, b, c)) - max(a, b, c)
print(max(a, b, c)*2**k + rem)