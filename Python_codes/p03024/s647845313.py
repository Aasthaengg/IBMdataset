s = str(input())
n = len(s)
x = s.count('o') + (15 - n)
ans = 'YES' if x >= 8 else 'NO'
print(ans)