a,p=map(int,input().split())
p+=a*3
apple_pie=0
while(p>=2):
    p-=2
    apple_pie+=1
print(apple_pie)