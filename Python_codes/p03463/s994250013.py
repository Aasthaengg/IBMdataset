# coding: utf-8
# Your code here!
N,a,b=map(int,input().split())
M=N/2
while True:
    #print(a,b)
    #Aliceのターン
    if a+1<b:
        a+=1
    elif a+1==b:
        a-=1
        
    if a<=0:
        print('Borys')
        break
    #Bobのターン
    if a+1<b:
        b-=1
    elif a+1==b:
        b+=1
        
    if b>N:
        print('Alice')
        break