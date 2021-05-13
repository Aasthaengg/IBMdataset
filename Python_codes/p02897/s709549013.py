N = int(input())

if 2 <= N and N%2 == 0:
    print(((N//2)/N))

elif 2<=N and N%2 != 0:
    print(((N+1)//2)/N)

else:
    print("1.00000")