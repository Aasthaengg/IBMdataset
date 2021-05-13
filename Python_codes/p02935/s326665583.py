N = int(input())
li = list(map(int, input().split()))
li.sort()
an = (li[0] + li[1])/2
for i in range(2,N):
    an = (an+li[i])/2
if an.is_integer():
 print(int(an))
else:
    print(an)