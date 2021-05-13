a,b,c = map(int,input().split())

dont_eat = max(c -(a+b)-1 ,0)

print(b+c-dont_eat)