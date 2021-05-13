N = int(input())
D,X = map(int,input().split())
A = [int(input()) for _ in range(N)]
sum_chocolate = X
for a in A:
  sum_chocolate += (D-1)//a+1
print(sum_chocolate)