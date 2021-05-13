a,b =map(int,input().split())
for i in range(1,1001):
        if 8*i//100 == a and i//10 == b:
                print(i)
                exit()
print('-1')