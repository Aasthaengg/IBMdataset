s = input(); n = len(s); a = [-1]*26; b = [0]*26
for i in range(n): j = ord(s[i])-97; b[j] = max(b[j], i-a[j]-1); a[j] = i
for i in range(26): b[i] = max(b[i], n-a[i]-1)
print(min(b))