n=int(input())
a = [int(input()) for _ in range(n)]
b = max(a)
c = a.index(b)
for i in range(n):
        if i == c:
                print(max(sorted(a)[:n-1]))
        else:
                print(b)