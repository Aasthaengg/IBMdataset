n = int(input())
alist = list(map(int,input().split()))
num_b = [0]*(n+1)
for i in range(n-1):
    num_b[alist[i]] += 1 
for i in range(1,n+1):
    print(num_b[i])