import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n, m = inintm()

kyoutu = []

for i in range(1,31):
    kyoutu.append(i)

for _ in range(n):
    A = inintl()
    t = A[1:]
    kyoutu = set(kyoutu) & set(t)

print(len(kyoutu))