N = int(input())
P = sorted([int(input()) for X in range(0,N)])
P[-1] = P[-1]//2
print(sum(P))