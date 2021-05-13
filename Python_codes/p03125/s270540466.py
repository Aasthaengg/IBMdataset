a,b= map(int,input().split())

for i in range(21):
    if a*i == b:
        print(a+b)
        exit()
print(b-a)
