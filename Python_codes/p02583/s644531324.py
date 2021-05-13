import itertools
N = int(input())
l = map(int,input().split())

cnt = 0
for a,b,c in itertools.combinations(l,3):
    if abs(a-b) < c < a+b and len(set([a,b,c])) == 3:
        cnt += 1

print(cnt)