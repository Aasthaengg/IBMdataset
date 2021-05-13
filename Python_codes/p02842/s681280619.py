N = int(input())
t = int(N/1.08)
if(t*1.08 == N):
    print(t)
elif(int((t+1)*1.08) == N):
    print(t+1)
elif(int((t-1)*1.08) == N):
    print(t-1)
else:
    print(':(')