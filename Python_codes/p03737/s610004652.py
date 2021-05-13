s = list(input().split())
ans = []
for i in s:
    ans.append(i[:1])
print(''.join(ans).upper())