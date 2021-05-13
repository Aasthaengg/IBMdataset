n,k = map(int,input().split())
s = input()
s = s[:k-1] + chr(ord(s[k-1])+ord('a')-ord('A')) + s[k:]
print(s)
