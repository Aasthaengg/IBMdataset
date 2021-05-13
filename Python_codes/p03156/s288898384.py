N = int(input())
A,B = map(int,input().split())
P = [int(x) for x in input().split()]

n1 = sum(1 if x <= A else 0 for x in P)
n2 = sum(1 if A < x <= B else 0 for x in P)
n3 = sum(1 if B < x else 0 for x in P)
answer = min(n1,n2,n3)
print(answer)