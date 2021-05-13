number=int(input().rstrip())
A,B=input().rstrip().split()
score=input().rstrip().split()
score=list(map(int,score))

score.append(int(A)+1)
score.append(int(B)+1)
score.sort()
n1=score.index(int(A)+1)
n2=score.index(int(B)+1)-score.index(int(A)+1)-1
n3=number-score.index(int(B)+1)+1
#print(n1)
#print(n2)
#print(n3)
#print(score)
print(min(n1,n2,n3))