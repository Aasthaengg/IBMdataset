n=int(input())
s = input()
ls = len(s)
ans = 0
for i in range(1,ls+1):
    ans = max(ans, s[:i].count('I')-s[:i].count('D'))
print(ans)