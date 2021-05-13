s = list(map(int, input().split()))
ss = sorted(s)

if ss[1]==ss[2]:
    print(ss[0])
else:
    print(ss[2])