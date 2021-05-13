s = input()
k = int(input())

if len(set(list(s))) == 1:
    print(len(s)*k//2)
    exit()

tmp = []
cnt = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        cnt += 1
    else:
        tmp.append(cnt)
        cnt = 1

tmp.append(cnt)

if s[0] != s[-1]:
    ans = [i//2 for i in tmp]
    print(sum(ans) * k)
else:
    a = tmp[0]//2
    b = (tmp[0] + tmp[-1])//2
    c = tmp[-1]//2
    ans = [i//2 for i in tmp[1:-1]]
    print(a+sum(ans)*k+b*(k-1)+c)