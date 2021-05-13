import math
n=int(input())
def s_bunkai(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr
if n%2==0:
    print(n,n,n//2)
else:
    num=s_bunkai(n)
    num2=num[0][0]
    if (num2+1)%4==0:
        num3=(num2*2+2)//4
        num4=n*num3
        print(num4//2,num4//num2,num4//num2)
    else:
        yn=0
        for i in range(len(num)):
            if num[i][0]%4==3:
                num2=num[i][0]
                yn=1
                break
        if yn==1:
            num3=(num2*2+2)//4
            num4=n*num3
            print(num4//2,num4//num2,num4//num2)
        else:
            yn=0
            for i in range(n//4,3501):
                for j in range(i,3501):
                    num5=(i*j)//math.gcd(i,j)
                    if num5%n==0:
                        num6=(num5//n)*4
                        num7=num6-(num5//i)-(num5//j)
                        if num5%num7==0 and num7>0:
                            print(i,j,num5//num7)
                            yn=1
                            break
                if yn==1:
                    break
