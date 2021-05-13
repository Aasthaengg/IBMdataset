n = int(input())
minn = 10**16
for i in range(5):
    minn = min(minn, int(input()))
print((n-1) // minn + 5)
