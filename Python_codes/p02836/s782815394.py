s = input()
cnt = 0
for i in range(len(s)//2):
    a0, a1 = s[i], s[-i-1]
    if a0 != a1:
        cnt += 1
print(cnt)
    
