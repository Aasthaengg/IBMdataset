h = int(input())
w = int(input())
n = int(input())
a = max(h, w)
if n%a == 0:
    print(n//a)
else:
    print(n//a + 1)