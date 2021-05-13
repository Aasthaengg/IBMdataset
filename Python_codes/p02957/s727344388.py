A,B = map(int,input().split())
answer = 'IMPOSSIBLE'
if (A+B)%2==0:
    answer = (A+B)//2
    
print(answer)