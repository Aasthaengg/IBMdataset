"""Boot-camp-for-Beginners_Easy005_B_Can-you-solve-this_25-August-2020.py"""

N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = list(list(map(int, input().split())) for i in range(N))

count=0
for i in range(N):
    s=0
    for j in range(len(B)):
        s+=B[j]*A[i][j]
    if s+C>0:
        count+=1
print(count)