import sys
def input(): return sys.stdin.readline().rstrip()
def I(): return int(input())
def Is(): return (int(x) for x in input().split())
def LI(): return list(Is())

# ----------------------------------------------------------- #

n = I()
B = LI()

ANS = []
for _ in range(n):
    for i in reversed(range(len(B))):
        if i+1 == B[i]:
            ANS.append(B.pop(i))
            break
    else:
        print(-1)
        exit()

ANS.reverse()
for ans in ANS:
    print(ans)
