N = int(input())
A,B = map(int,input().split())
P = list(map(int,input().split()))
C = [0 for i in range(3)]
for i in range(N):
    a = P[i]
    if a<=A:
        C[0] += 1
    elif A+1<=a<=B:
        C[1] += 1
    elif a>=B+1:
        C[2] += 1
print(min(C))