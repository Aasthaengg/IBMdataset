# coding:utf-8

n=input()

while True:
    if n=="-":
        break
        
    m=int(input())

    for i in range(0,m):
        t=int(input())
        n=n[t:-1]+n[-1]+n[0:t]

    print(n)

    n=input()