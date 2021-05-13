N = int(input())
D,X = map(int,input().split())
A = [int(input()) for i in range(N)]

C = sum([(D-1)//a + 1 for a in A])

print(C+X)
