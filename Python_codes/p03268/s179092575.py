n, k = map(int, input().split())
N = [i%k for i in range(1,n+1)]
if k%2==0:
    print(pow(sum([1 for i in N if i==0]), 3)+pow(sum([1 for i in N if i==k//2]),3))
else:
    print(pow(sum([1 for i in N if i==0]), 3))