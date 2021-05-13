k = int(input())
s = input()

if k >= len(s):
    print(s)
else:
    tmp = s[0:k]
    tmp = tmp + "..."
    print(tmp)