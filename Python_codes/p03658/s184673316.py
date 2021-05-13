N,K = map(int,input().split())

A = list(map(int,input().split()))
A.sort()

tar = A[-K:]
tar_sum = sum(tar)
print(tar_sum)