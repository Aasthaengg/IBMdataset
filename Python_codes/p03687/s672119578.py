s = '_'+input()
l = len(s)
dist_lst = [0]*26
idx_lst = [0]*26
for i in range(1,l):
    c = ord(s[i])%26
    dist_lst[c] = max(dist_lst[c],i-idx_lst[c])
    idx_lst[c] = i
for c in range(26):
    dist_lst[c] = max(dist_lst[c],l-idx_lst[c])

print(min(dist_lst)-1)