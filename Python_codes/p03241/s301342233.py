def cd_generator(num):
    i=1
    lower=[]
    upper=[]
    while i*i<=num:
        if num%i==0:
            lower.append(i)
            if num!=i*i:
                upper.append(num//i)
        i+=1
    return reversed(lower+upper[::-1])
n,m=map(int,input().split())

for ele in cd_generator(m):
    if m/ele>=n:
        print(ele)
        exit()
