a,b,c,d=map(int,input().split())
X=c-a
Y=d-b
ans1='R'*X+'U'*Y
ans2='L'*X+'D'*Y
ans3='D'+'R'*(X+1)+'U'*(Y+1)+'L'
ans4='U'+'L'*(X+1)+'D'*(Y+1)+'R'
print(ans1+ans2+ans3+ans4)