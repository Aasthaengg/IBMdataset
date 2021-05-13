def intMap(): return map(int,input().split())

n,k = intMap()
s = input()

ans = s[:k-1] + s[k-1].lower() + s[k:]
print(ans)
