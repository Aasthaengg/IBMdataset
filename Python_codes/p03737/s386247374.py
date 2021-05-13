a = input().split()
ans = []
for i in range(len(a)):
    b = chr(ord(a[i][0])-32)
    ans.append(b)
print(''.join(ans))