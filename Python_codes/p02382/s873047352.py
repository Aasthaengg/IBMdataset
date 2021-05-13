from math import sqrt

n = int(input())
vector1 = map(int,input().split())
vector2 = map(int,input().split())
diffs = [abs(x-y) for x,y in zip(vector1,vector2)]
print (sum(diffs))
print (sqrt(sum(map(lambda n:pow(n,2),diffs))))
print ((sum(map(lambda n:pow(n,3),diffs)))**(1/3))
print (max(diffs))