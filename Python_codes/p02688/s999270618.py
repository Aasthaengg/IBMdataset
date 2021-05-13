n,k = map(int,input().split())

judge = [True] * n
for i in range(k):
    j = int(input())
    A = list(map(int,input().split()))
    for a in A:
        judge[a-1] = False

print(judge.count(True))
