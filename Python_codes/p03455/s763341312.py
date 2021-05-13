import sys
stdin = sys.stdin
#n = int(stdin.readline().rstrip())
#l = list(map(int, stdin.readline().rstrip().split()))
a,b = map(int, stdin.readline().rstrip().split())

c = a * b
if c % 2 == 1:
    print("Odd")
else:
    print("Even")
