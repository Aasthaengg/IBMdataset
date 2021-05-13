import sys
K = int(input())

x = 7
for ans in range(1, K*2):

    if  x%K == 0:
        print(ans)
        sys.exit()

    x = (x*10 + 7) % K
print(-1)