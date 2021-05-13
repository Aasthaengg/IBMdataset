n = int(input())
a = list(map(int, input().split()))
s = sorted(a)
A = 0
B = 0
for i in range(n-1, -1, -1):
    if n%2 == 0:
        if i%2 == 0:
            B += s[i]
        else:
            A += s[i]
    else:
        if i%2 == 0:
            A += s[i]
        else:
            B += s[i]
print(A - B)