a = input()
n = len(a)
mp = [0]*26
for c in a:
    mp[ord(c) - ord('a')] += 1
t = sum([n*(n-1)/2 for n in mp])
print(int(n*(n-1) / 2 - t + 1))