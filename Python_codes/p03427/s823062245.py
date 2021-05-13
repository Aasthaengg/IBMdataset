n = input()
m = int(n)
c = n[0]
k = len(n)
tmp = int(c + "9"*(k-1))
ans = int(c) + (k-1)*9
if tmp > m:
    ans = (int(c)-1) + (k-1)*9
print(ans)