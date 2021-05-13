s = input()
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

n = len(s)
ans = n

for v in alphabet:
    key = [s[i] for i in range(n)]
    
    count = 0
    end = False
    while True:
        for i in range(n-count):
            if key[i] != v:
                break
            if i == n-count-1:
                ans = min(ans, count)
                end = True
        if count == n-1:
            break
        
        if end:
            break
        
        count += 1
        for i in range(n-count):
            if key[i] == v or key[i+1] == v:
                key[i] = v

print(ans)