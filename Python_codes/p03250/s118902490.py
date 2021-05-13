N = list(map(int,input().split()))
N.sort(reverse=True)
print(N[0]*10 + sum(N[1:]))