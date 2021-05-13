x=int(input())
c=(x+100-1)//100
# print(c)
for i in range(1,c+1):
    if 100*i<=x<=105*i:
        print(1)
        exit()
else : print(0)