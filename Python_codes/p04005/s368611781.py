import itertools

l = list(map(int, input().split()))
ans = 0

if all(elem %2 ==1 for elem in l):
    l.sort()
    ans = l[0] * l[1]
    
print(ans)

