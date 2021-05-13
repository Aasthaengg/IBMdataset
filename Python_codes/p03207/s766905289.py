N=int(input())
P=[int(input()) for i in range(N)]
print(int((sorted(P)[-1]/2)+sum(sorted(P)[:-1])))