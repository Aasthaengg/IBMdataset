s = list(map(int,input().split()))

for i in set(s):
    if s.count(i) == 1:
        print(i)