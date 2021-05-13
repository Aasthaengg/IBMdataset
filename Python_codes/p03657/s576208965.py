a,b=map(int,input().split())
print('Possible') if a+b>=3 and (a%3==0 or b%3==0 or (a+b)%3==0) else print('Impossible')