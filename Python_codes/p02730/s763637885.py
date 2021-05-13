a = input()
l = len(a)
m = a[:l//2]
n = a[l//2 + 1 :]
if a[::-1] == a and m == m[::-1] and n == n[::-1]:
    print("Yes")
else:
    print("No")