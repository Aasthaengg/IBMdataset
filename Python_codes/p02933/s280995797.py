import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


# inputna
n = int(input())
s = input()
if n>=3200:
    print(s)
else:
    print("red")