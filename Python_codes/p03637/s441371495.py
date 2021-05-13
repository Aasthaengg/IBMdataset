N = int(input())

a = list(map(int, input().split()))

odd_count = 0
four_count = 0

ans = 'Yes'

for i in a:
    if i % 2 == 1:
        odd_count += 1
    if i % 4 == 0:
        four_count += 1

if len(a) % 2 == 0:
    if odd_count > four_count:
        ans = 'No'
else:
    if odd_count <= four_count or len(a) == odd_count + four_count and odd_count -1 <= four_count:
        pass
    else:
        ans = 'No'

print(ans)
