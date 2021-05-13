n, a, b = map(int, input().split())
if a%2==b%2:
    print((b-a)//2); exit()
ans1 = 0
c = a
aa = 1
bb = b-a
ans1 = c
if aa!=bb:
    ans1 += (bb-aa)//2
ans2 = 0
c = n-b+1
bb = n
aa = a+c
ans2 = c
if aa!=bb:
    ans2 += (bb-aa)//2
print(min(ans1, ans2))