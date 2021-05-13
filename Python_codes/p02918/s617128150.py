n,k = map(int,input().split())
s = list(input())

first = s[0]
second = 'R' if first=='L' else 'L'

i = 0
while k > 0 and i < n:
    if s[i] ==second:
        while i < n and  s[i] == second:
            s[i] = first
            i += 1
        k -= 1
    else:
        i += 1

# print(s)

ans = 0

def happy_check(i):
    global ans
    if i < n-1 and s[i] == 'R' and s[i+1] == 'R':
        ans += 1
    elif 0 < i and s[i] == 'L' and s[i-1] == 'L':
        ans += 1

for i in range(n):
    happy_check(i)

print(ans)