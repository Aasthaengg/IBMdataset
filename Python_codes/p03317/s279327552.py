N,K = map(int, input().split())
A=list(map(int,input().split()))

min_num=min(A)
count=A.count(min_num)
target=len(A)-count
K_num=K-1

print(int(-(-target//K_num)))