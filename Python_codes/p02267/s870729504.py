n = int(input())
S = [int(s) for s in str(input()).split()]
q = int(input())
T = [int(t) for t in str(input()).split()]
#print(n, S, q, T)

print(len([i for i in T if i in S]))