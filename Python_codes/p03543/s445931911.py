import sys
N = int(input())
N2 = list(map(int,str(N)))
if not (1000 <= N <= 9999):
    sys.exit()

if N2[0] == N2[1] == N2[2] or N2[1] == N2[2] == N2[3]:
    print("Yes")
else:
    print("No")
