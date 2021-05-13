N = int(input())
Data = list(map(int,input().split()))
Dic = {}
for d in Data:
    if not d in Dic:
        Dic[d] = 0
    Dic[d]+=1

even = 0
odd  = 0
for k,v in Dic.items():
    if v % 2 == 0:
        even += 1
    else:
        odd += 1

if even % 2 == 0:
    ans = even + odd
else:
    ans = even + odd -1

print(ans)
