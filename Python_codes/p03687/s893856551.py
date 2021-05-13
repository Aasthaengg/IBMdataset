from collections import Counter
s = input()

def f(s, c):
    n = len(s)
    if not c in s:
        return n-1
    else:
        longest = 0
        last = -1
        i = 0
        while i < n:
            l = 0
            while i < n and s[i]!=c:
                l+=1 
                i+=1
            if i < n and s[i]==c:
                last = i
                longest = max(longest, l)
            i+=1
        return max(n-last-1, longest)

ans = float('inf')
for i in range(26):
    c = chr(ord('a')+i)
    ans = min(ans, f(s, c))
print(ans)