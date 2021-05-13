N = int(input())
K = int(input())
print(sum([2*min(x,K-x) for x in list(map(int,input().split()))]))