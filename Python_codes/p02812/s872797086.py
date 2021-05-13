n = int(input())
s = str(input())
cnt = 0
for i in range(n-2):
    if s[i:3+i] == 'ABC':
        cnt += 1
print(cnt)
