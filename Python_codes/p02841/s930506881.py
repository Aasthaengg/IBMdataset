from sys import stdin
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
#n = int(stdin.readline().rstrip())
#l = list(map(int, stdin.readline().rstrip().split()))
M1, D1 = map(int, stdin.readline().rstrip().split())
M2, D2 = map(int, stdin.readline().rstrip().split())
#S = [list(stdin.buffer.readline().decode().rstrip()) for _ in range(h)]

if M1 != M2:
    print(1)
else:
    print(0)
