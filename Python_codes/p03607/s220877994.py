import collections as c
print(sum([1 for i in c.Counter([int(input()) for _ in range(int(input()))]).values() if i%2!=0]))