k = int(input())
A = list(map(int, input().split()))
UP = 2
DOWN = 2 
for a in A[::-1]:
  DOWN = ((DOWN - 1) // a + 1) * a
  UP = UP // a * a + a  - 1
  if UP < DOWN:
    print(-1)
    exit()
print(DOWN, UP)