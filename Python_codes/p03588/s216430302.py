N = int(input())
max_A = 0
score = 0
for _ in range(N):
    A,B = [int(x) for x in input().split()]
    if(max_A<A):
        max_A = A
        score = B
print(max_A + score)