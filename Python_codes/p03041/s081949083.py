n,k = map(int,input().split())
s = input()
t = chr(ord(s[k - 1]) + 32)
s = s[:k-1] + t + s[k:]
print(s)