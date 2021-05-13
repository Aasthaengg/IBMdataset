sx = input()
x = int(sx)

ans = 1001001001
for i in range(len(sx)-2):
    t = int(sx[i:i+3])
    a = abs(753 - t)
    ans = min(ans, a)
    
print(ans)