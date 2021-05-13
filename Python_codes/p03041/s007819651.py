n, k = list(map(int, input().split()))
s = input()

first = s[:k-1]
mid = s[k-1].lower()
last = s[k:]

print( first + mid + last )
