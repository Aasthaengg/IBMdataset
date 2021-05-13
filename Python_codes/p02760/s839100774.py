card = []
check = [False for i in range(9)]
for i in range(3):
  card += list(map(int, input().split()))
N = int(input())
for i in range(N):
  a = int(input())
  if a in card:
    check[card.index(a)] = True
ans = "No"
for i in range(3):
  if check[i] and check[3+i] and check[6+i]:
    ans = "Yes"
  if check[i*3] and check[i*3+1] and check[i*3+2]:
    ans = "Yes"
if check[4] and ((check[0] and check[8])or(check[2] and check[6])):
  ans = "Yes"
  
print(ans)