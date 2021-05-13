#Palindromic Numbers
a,b = map(int, input().split())
#12345
ans1=0
ans5=0
ans2=0
ans4=0
ans3=0
n=0
for i in range(a,b+1):
    ans5=i%10
    ans4=(i//10)%10
    ans3=(i//100)%10
    ans2=(i//1000)%10
    ans1=(i//10000)%10
    if ans5 == ans1:
        if  ans4 == ans2:
            n+=1
print(n)

