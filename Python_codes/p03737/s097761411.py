a = list(map(str,input().split()))
ans = []

for i in range(3):
    tmp = list(map(str,a[i]))
    b = tmp[0]
    b = chr(ord(b)-32)
    ans.append(b)

print("".join(ans))