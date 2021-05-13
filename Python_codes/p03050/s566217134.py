N = int(input())
ans = 0
for i in range(1,min(N,1250000)):
    if(((N-i)/i).is_integer() and N//((N-i)/i) == N%((N-i)/i)):
        # print((N-i)//i,i)
        ans += ((N-i)//i)
        # if(i == 800000):
        #     print(ans)
    # print(i)
print(ans)