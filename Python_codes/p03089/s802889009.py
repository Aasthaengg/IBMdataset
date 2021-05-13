import sys

N = int(input())
#Bs = list(map(int, input().split()))
Bs = [B - 1 for B in map(int, input().split())]

anss = []
for _ in range(N):
    iNow = -1
    for i in reversed(range(len(Bs))):
        if Bs[i] == i:
            iNow = i
            break
    else:
        print(-1)
        sys.exit()

    anss.append(iNow)

    Bs = Bs[:iNow] + Bs[iNow+1:]

print('\n'.join(map(str, [ans+1 for ans in anss[::-1]])))
