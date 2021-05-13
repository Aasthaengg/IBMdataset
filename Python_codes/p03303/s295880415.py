s = input()
w = int(input())
ans = []
for i in range(0,len(s),w):
    ans.append(s[i])
print(''.join(ans))
