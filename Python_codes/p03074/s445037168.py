n,k = map(int,input().split())
s = input()
now = 1
cnt = 0
Nums = []
for i in range(n):
    if s[i] == str(now): cnt += 1
    else:
        Nums.append(cnt)
        now = 1-now
        cnt = 1
if cnt != 0: Nums.append(cnt)

if len(Nums)%2 == 0: Nums.append(0)
ad = 2*k+1
# print(Nums)
ans = 0
left = right = 0
tmp = 0
for i in range(0,len(Nums),2):
    nextleft = i
    nextright = min(i+ad, len(Nums))
    while nextleft > left:
        tmp -= Nums[left]
        left += 1
    while nextright > right:
        tmp += Nums[right]
        right += 1
    ans = max(tmp,ans)
print(ans)