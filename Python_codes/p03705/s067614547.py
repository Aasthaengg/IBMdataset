n,a,b = map(int,input().split())

if n == 1 and a != b or a > b:
    print(0)
    exit()

print(1+a+(n-1)*b-((n-1)*a+b))