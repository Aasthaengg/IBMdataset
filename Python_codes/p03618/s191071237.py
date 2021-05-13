import collections
A= input()
Ac = collections.Counter(A)
cnt = 0
for val in Ac.values():
    cnt += val*(val-1)//2
print(len(A)*(len(A)-1)//2-cnt+1)
