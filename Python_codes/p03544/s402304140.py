import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())


n = inint()

ryuka = [2,1]

for i in range(2,87):
    ryuka.append(ryuka[i-1]+ryuka[i-2])

print(ryuka[n])