N,M=map(int,input().split())
ans1=[]
ans2=[]
ans3=[]
ans4=[]
ans5=[]
ans6=[]
ans7=[]
ans8=[]

ANS1=0
ANS2=0
ANS3=0
ANS4=0
ANS5=0
ANS6=0
ANS7=0
ANS8=0


for i in range(N):
    A,B,C=map(int,input().split())
    
    ans1.append(A+B+C)
    ans2.append(-A+B+C)
    ans3.append(A-B+C)
    ans4.append(A+B-C)
    ans5.append(-A-B+C)
    ans6.append(A-B-C)
    ans7.append(-A+B-C)
    ans8.append(-A-B-C)
    
re_ans1=sorted(ans1)
re_ans2=sorted(ans2)
re_ans3=sorted(ans3)
re_ans4=sorted(ans4)
re_ans5=sorted(ans5)
re_ans6=sorted(ans6)
re_ans7=sorted(ans7)
re_ans8=sorted(ans8)
for j in range(1,M+1):
    ANS1+=re_ans1[(-1)*j]
    ANS2+=re_ans2[(-1)*j]
    ANS3+=re_ans3[(-1)*j]
    ANS4+=re_ans4[(-1)*j]   
    ANS5+=re_ans5[(-1)*j]
    ANS6+=re_ans6[(-1)*j]
    ANS7+=re_ans7[(-1)*j]
    ANS8+=re_ans8[(-1)*j]
print(max(ANS1,ANS2,ANS3,ANS4,ANS5,ANS6,ANS7,ANS8))