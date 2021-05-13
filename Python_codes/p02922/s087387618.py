a = input("").split(" ")
a = [int(b) for b in a]
A = a[0]
B = a[1]
n = 1
ans = 0
while n < B:
    ans += 1
    n += A-1
print(ans)