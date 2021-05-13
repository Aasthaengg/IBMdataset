from collections import Counter
N=int(input())

numbers=[]

for _ in range(N):
    A=int(input())
    numbers.append(A)

answers=Counter(numbers)

answer=0
for value in answers.values():
    if value%2==1:
        answer+=1
print(answer)
