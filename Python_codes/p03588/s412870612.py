N = int(input())
max_A = 0
min_B = 0
for i in range(N):
    A, B = list(map(int, input().split()))
    if(A > max_A):
        max_A = A
        min_B = B
print(max_A+min_B)