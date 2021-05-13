while True:
    n=int(input())
    if n==0:
        break
    lst=[int(i) for i in input().split()]
    m=sum(lst)/len(lst)
    a_2=0
    for l in range(n):
        value=lst[l]
        a_2+=pow(value-m,2)/n
    print(pow(a_2,0.5))
