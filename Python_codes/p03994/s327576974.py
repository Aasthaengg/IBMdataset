alf = {c:i for i,c in enumerate('abcdefghijklmnopqrstuvwxyz')}
a = 'abcdefghijklmnopqrstuvwxyz'
s = input()
k = int(input())
diff = [26-alf[c] if c != 'a' else 0 for c in s]
ans = []
for i in range(len(s)):
    if k >= diff[i]:
        ans.append('a')
        k -= diff[i]
    else:
        ans.append(s[i])
    # print(ans,k)
if k > 0:
    ans[-1] = a[(alf[ans[-1]] + k % 26)]
print(''.join(ans))
