#k = int(input())
s = input()
#a, b = map(int, input().split())
#l = list(map(int, input().split()))
t = input()
ans = "Yes"
for i in range(len(s)):
    if s[i] != t[i]:
        ans = "No"
        break
print(ans)
