n = int(input())
s = input().split()
for i in range(n-1, -1, -1):
    if i == 0:
        print(s[i])
    else:
        print(s[i], end=" ")