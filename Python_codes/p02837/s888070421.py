N=int(input())
numbers=[]
for _ in range(N):
    A=int(input())
    number=[]
    for _ in range(A):
        x,y=map(int,input().split())
        number.append([x,y])
    numbers.append(number)
answers=[]
for i in range(2**N):
    number=[]
    for j in range(N):
        if ((i>>j)&1):
            number.append(j+1)
    answers.append(number)
del answers[0]
ans=0
for answer in answers:
    kouho=[]
    num=0
    flag=0
    for a in answer:
        kouho+=numbers[a-1]
    for k in kouho:
        if k[1]==1 and k[0] not in answer:
            flag=1
            break
        elif k[1]==0 and k[0] in answer:
            flag=1
            break
    if flag==0:
        num=len(answer)
    ans=max(ans,num)
print(ans)

