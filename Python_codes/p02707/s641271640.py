n = int(input())
a = list(map(int,input().split()))
m = [0] * (n+1)
for i in a:
    m[i] += 1
for i in m[1:]:
    print(i)