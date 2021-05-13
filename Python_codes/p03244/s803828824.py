from collections import Counter
N=int(input())
v=list(map(int,input().split()))
even=[]
odd=[]
for n in range(N):
    if n%2==0:
        even.append(v[n])
    else:
        odd.append(v[n])
evens=Counter(even)
odds=Counter(odd)
even_value_max=max(evens.values())
odds_value_max=max(odds.values())
even_numbers=[]
odds_numbers=[]
for key,value in evens.items():
    if value==even_value_max:
        even_numbers.append(key)
for key,value in odds.items():
    if value==odds_value_max:
        odds_numbers.append(key)
if len(evens)==1 and len(odds)==1 and v[0]==v[1]:
    answer=N//2
elif len(even_numbers)>=2 or len(odds_numbers)>=2:
    answer=N-even_value_max-odds_value_max
else:
    even=even_numbers[0]
    odd=odds_numbers[0]
    if even!=odd:
        answer=N-even_value_max-odds_value_max
    else:
        evens[even]=0
        odds[odd]=0
        if max(odds.values())>=max(evens.values()):
            answer=N-max(odds.values())-even_value_max
        else:
            answer=N-max(evens.values())-odds_value_max
print(answer)
