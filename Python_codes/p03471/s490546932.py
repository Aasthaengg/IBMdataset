N,Y = map(int, input().split())
for i in range(Y//10000+1):
    for j in range((Y-10000*i)//5000+1):
        k = N-i-j
        if 10000*i+5000*j+1000*k==Y and k>=0:
            print(i, j, k)
            break
    else: 
        continue
    break
else:
    print(-1,-1,-1)