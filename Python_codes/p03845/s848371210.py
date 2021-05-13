N = int(input())
T = list(map(int, input().split()))
M = int(input())
Tex = [input().split() for i in range(M)]
for t in Tex:
    print(sum(T) - T[int(t[0])-1] + int(t[1]))