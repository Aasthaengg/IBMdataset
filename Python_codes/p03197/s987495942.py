n = int(input())
al = []
for _ in range(n):
    a = int(input())
    al.append(a)

if all(a % 2 == 0for a in al):
    print("second")
else:
    print("first")