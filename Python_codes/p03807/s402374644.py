n = int(input())
num_lists = list(map(int, input().split()))

odds = []
evens = []
for i in num_lists:
    if i%2 == 0:
        evens.append(i)
    else:
        odds.append(i)

odds_sum = 0
for i in odds:
    odds_sum += i

if odds_sum%2 == 0:
    ans = 'YES'
else:
    ans = 'NO'

print(ans)