N = int(input())
a_list = [int(a) for a in input().split()]

if a_list[0] > 1:
    print(-1)
    exit()

ans = 1
temp1 = [""]*(N+1)
temp1[-1] = a_list[-1]
for n in range(N-1, 0, -1):
    temp1[n] = temp1[n+1]+a_list[n]
    
temp2 = 1
for n in range(1, N+1):
    temp2 = (temp2-a_list[n-1])*2
#     print(temp2, temp1[n])
    ans_temp = min(temp2, temp1[n])
    temp2 = min(temp2, temp1[n])
    
    if ans_temp < a_list[n]:
        print(-1)
        exit()
    
    ans += ans_temp
    
print(ans)