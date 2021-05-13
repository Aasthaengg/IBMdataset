K = int(input())
A,B = map(int,input().split())
res = "NG"
for i in range (K, B+1, K):
  if A<= i <= B:
    res = "OK"
print(res)