n = int(input())
t, a = map(int , input().split())
hn = [int(num) for num in input().split()]

answers = []
for h in hn:
  answers.append(abs(a-(t-h*0.006)))
  
print(answers.index(min(answers))+1)