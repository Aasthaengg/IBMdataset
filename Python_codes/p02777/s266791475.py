s, t = map(str,input().split())
a, b= map(int,input().split())
u= str(input())

if s==u:
    a-=1

if t==u:
    b-=1
print('%d %d' % (a, b))