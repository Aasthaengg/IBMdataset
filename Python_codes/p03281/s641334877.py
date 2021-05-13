N = int(input())

if N >= 195:
    ans = 5
elif N >= 189:
    ans = 4
elif N >= 165:
    ans = 3
elif N >= 135:
    ans = 2
elif N >= 105:
    ans = 1
else:
    ans = 0

print(ans)
