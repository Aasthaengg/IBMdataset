#45
A,B = map(int,input().split())
cnt = 0
num1,num2 = "",""
for i in range(A,B+1):
    num1 = str(i)
    num2 = num1[::-1]
    if num1 == num2:
        cnt +=1
        
print(cnt)