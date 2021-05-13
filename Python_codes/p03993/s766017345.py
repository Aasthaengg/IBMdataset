n = int(input())
al = list(map(int,input().split()))

ans = 0
for idx,a in enumerate(al):
   if al[a-1]-1 == idx:
      ans += 1
print(ans//2)