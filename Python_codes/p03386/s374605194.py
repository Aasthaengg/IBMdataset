a,b,k = map(int,input().split())

for i in range(a,a+k):
    if a <= i and i <= b:
        print(i)

for i in range(b-k+1,b+1):
    if i not in range(a,a+k):
        if a <= i and i <= b:
            print(i)