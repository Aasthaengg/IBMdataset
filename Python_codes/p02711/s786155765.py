N = int(input())

digit = []

div_num = 10

while(True):
    digit.append(N % div_num)
    if(N % div_num == N):
        break;
    N //= div_num 

if 7 in digit:
    print("Yes")
else:
    print("No")