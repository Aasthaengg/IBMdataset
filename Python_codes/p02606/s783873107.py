L,R,D = map(int, input().split())

r = [i for i in range(L,R+1)]

N = [k for k in r if k % D == 0]

print(len(N))