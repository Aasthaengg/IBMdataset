a =int(input())
b= int(input())
c= int(input())
d= int(input())
e= int(input())
A = abs(a%10-10)
B = abs(b%10-10)
C = abs(c%10-10)
D = abs(d%10-10)
E = abs(e%10-10)
lst= [A,B,C,D,E]
ad = 0
cnt = 0
for i in lst:
    if (i != 10) and (i>ad):
        ad = i
    if i == 10:
        cnt += 1
ans = (a//10+b//10+c//10+d//10+e//10+5-cnt)*10-(ad)
print(ans)