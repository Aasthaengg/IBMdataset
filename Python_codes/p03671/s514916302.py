a,b,c=map(int,input().split())
answer = float('inf')
if a+b<=answer:
    answer=a+b
if c+b<=answer:
    answer=c+b
if a+c<=answer:
    answer=a+c
print(answer)    