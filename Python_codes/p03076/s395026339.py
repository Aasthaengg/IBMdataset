import itertools
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

ans = 10**9
for v in itertools.permutations([a,b,c,d,e],5):
    time = 0
    for i in range(4):
        time += v[i]
        amari = time % 10
        if amari != 0:
            time += 10 - amari
    time += v[4]
    ans = min(ans,time)

print(ans)