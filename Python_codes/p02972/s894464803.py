from collections import deque
N=int(input())
A=list(map(int,input().split()))
reverse_A=list(reversed(A))
numbers=[]
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
boxes=[0 for _ in range(N)]
for n in range(N):
    yakusuu=make_divisors(n+1)
    numbers+=[yakusuu]
reverse_numbers=list(reversed(numbers))
answers=[0 for _ in range(N)]
balls=[0 for _ in range(N)]
for n in range(N-1):
    number=reverse_numbers[n]
    if balls[n]%2==0 and reverse_A[n]==1:
        answers[n]+=1
        for num in number:
            balls[-num]+=1
    elif balls[n]%2==1 and reverse_A[n]==0:
        answers[n] += 1
        for num in number:
            balls[-num] += 1
if sum(answers)%2==0 and reverse_A[-1]==1:
    answers[-1]+=1
elif sum(answers)%2==1 and reverse_A[-1]==0:
    answers[-1]+=1
print(sum(answers))
reverse_answers = list(reversed(answers))
kotae = []
for n in range(N):
    if reverse_answers[n] != 0:
        kotae.append(n + 1)
print(*kotae)
