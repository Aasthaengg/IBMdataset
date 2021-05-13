s = list(input())
alphcnt = [0] * 3
for i in s:
    alphcnt[ord(i) - 97] += 1
print("YES" if max(alphcnt) - min(alphcnt) <= 1 else "NO")