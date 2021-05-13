s = input()
k = 'keyence'
k_size = len(k)
d_size = len(s) - k_size

result = "NO"
for i in range(k_size):
    t = s[:i] + s[i+d_size:]
    if t == k:
        result = "YES"
        break
print(result)