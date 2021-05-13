from collections import Counter

def solve():
    N = int(input())
    a = list(map(int, input().split()))
    
    if len(set(a)) == 1 and a[0] == 0:
        return 'Yes'
    
    if N % 3 == 0:
        s = list(set(a))
        c = Counter(a)
        if len(s) == 2:
            i = max(c.items(), key=lambda x: x[1])
            j = min(c.items(), key=lambda x: x[1])
            if i[0] ^ j[0] == i[0] and i[1] == (2 * N // 3) and j[1] == (N // 3):
                return 'Yes'
        if len(s) == 3:
            if c[s[0]] == c[s[1]] and c[s[1]] == c[s[2]] and s[0] ^ s[1] == s[2]:
                return 'Yes'
        
    return 'No'

print(solve())