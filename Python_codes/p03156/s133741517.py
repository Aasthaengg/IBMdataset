N = int(input())
A,B = [int(i) for i in input().split()]
P = [int(i) for i in input().split()]
am = 0
ab = 0
bu = 0
for i in range(N):
    if P[i]<=A:
        am+=1
    if A+1<=P[i]<=B:
        ab +=1
    if B+1<=P[i]:
        bu+=1

print(min(am,ab,bu))