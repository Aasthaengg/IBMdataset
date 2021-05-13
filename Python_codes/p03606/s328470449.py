N=int(input())
answers=[]
for a in range(N):
    l,r=input().split()
    answer=int(r)-int(l)+1
    answers.append(answer)
print(sum(answers))
