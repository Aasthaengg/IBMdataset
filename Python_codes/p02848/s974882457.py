n = int(input())
S = input()

tmp = []
for s in S:
    if ord(s)+n > ord('Z'):
        tmp.append(ord('A')+(ord(s)+n)%ord('Z')-1)
    else:
        tmp.append(ord(s)+n)

ans = ''
for i in tmp:
    ans += chr(i)
print(ans)