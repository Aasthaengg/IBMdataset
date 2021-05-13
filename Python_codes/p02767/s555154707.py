N = int(input())
X = list(map(int,input().split()))
p = round(sum(X)/len(X))
print(sum([(x-p)**2 for x in X]))