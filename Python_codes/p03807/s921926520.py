N = int(input())
A = list(map(int,input().split()))
Odds = list(filter(lambda x:x%2 == 1,A))
Odds_num = len(Odds)
if Odds_num % 2 == 1:
    print("NO")
else:
    print("YES")