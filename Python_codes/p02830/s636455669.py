N = int(input())
S, T = map(str, input().split())
lst = []

for i in range(N):
    lst.append(S[i])
    lst.append(T[i])

for i in lst:
    print(i,end='')