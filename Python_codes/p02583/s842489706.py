import itertools
N = int(input())
l = map(int,input().split())

cnt = 0
for a,b,c in itertools.combinations(l,3):
    if abs(a-b) < c < a+b and a != b and b != c and a != c:
        cnt += 1

print(cnt)