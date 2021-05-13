k = int(input())
s = input()
l = len(s)

print(s if l <= k else s[:k]+"...")