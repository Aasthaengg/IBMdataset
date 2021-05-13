n=int(input())
a=list(map(int,input().split()))

al = 0
for x in a:
    al^=x
ans = [0]*n

for i in range(n):
    ans[i] = al^a[i]

print(" ".join([str(d) for d in ans]))