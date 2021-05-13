N = list(map(int,input().split()))
M = (N[2] - N[1]) * (N[0] - 2) + 1
if N[0] == 1 and N[1] == N[2]:
    print(1)
elif N[0] == 1:
    print(0)
elif N[0] == 2:
    print(1)
elif N[1] > N[2]:
    print(0)
else:
    print(M)