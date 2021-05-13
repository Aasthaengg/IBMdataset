k = int(input())
s = input()
t = s[0]
if len(s) <= k:
    print(s)
else:
    for i in range(1, k):
        t += s[i]
    print(t + '...')
