import collections
N = int(input())
number = list(map(int,input().split()))
number = collections.Counter(number)
for i in range(1,N+1):
    if i in number:
        print(number[i])
    else:
        print("0")
