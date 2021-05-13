import collections
N = int(input())

Boss = [int(x) for x in input().split()]
kind_of_Boss = collections.Counter(Boss)

for i in range(1,N):
    print(kind_of_Boss[i])
    
print(0)