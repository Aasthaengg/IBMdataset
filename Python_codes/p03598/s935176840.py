n = int(input())
k = int(input())
xn = [int(num) for num in input().split()]

answers = []
for x in xn:
  answers.append(2*min(x,k-x))
   
print(sum(answers))
