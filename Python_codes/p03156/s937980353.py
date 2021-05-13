N = int(input())
A,B = map(int,input().split())
P = list(map(int,input().split()))
ls1 = []
ls2 = []
ls3 = []
for i in range(N):
    if P[i]<=A:
        ls1.append(P[i])
    elif (A+1)<=P[i]<=B:
        ls2.append(P[i])
    else:
        ls3.append(P[i])
print(min(len(ls1),len(ls2),len(ls3)))