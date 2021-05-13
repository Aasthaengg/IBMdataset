s = input()
ans = 753

for i in range(len(s)-2):
    num = int(s[i:i+3])
    gap = abs(753-num)

    if gap < ans:
        ans = gap
    
print(ans)