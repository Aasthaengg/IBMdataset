from collections import Counter
n = int(input())
A = sorted(list(map(int,input().split())))
c = list(Counter(A).values())
ans = len(c)
d = [i-1 for i in c]
print(ans if sum(d)%2==0 else ans-1)