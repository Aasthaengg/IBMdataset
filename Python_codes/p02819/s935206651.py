a=int(input())
def judge(n):
    if n==2:
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                break
            elif i*i>n:
                return True
while True:
    if judge(a)==True:
        print(a)
        break
    a+=1