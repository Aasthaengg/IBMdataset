A,B=map(int,input().split())
for i in range(1,10**7):
    if A==int(i*0.08) and B==int(i*0.1):
        print(i)
        exit()
print(-1)