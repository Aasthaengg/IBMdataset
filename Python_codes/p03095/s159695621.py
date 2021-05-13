n = int(input()); s = input()
a = [0]*26; b = 1
for i in range(n): a[ord(s[i])-97] += 1
for i in range(26): b *= a[i]+1
print((b-1)%(10**9+7))