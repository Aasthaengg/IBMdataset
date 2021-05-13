N = int(input())
a = int(str(N)[0] * 3)
if N == a:
    print(N)
elif N < a:
    print(a)
else:
    print(a + 111)