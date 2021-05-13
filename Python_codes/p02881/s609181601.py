N = int(input())
mn = N
for i in range(1,int(pow(N,0.5))+1):
    if N%i == 0:
        d = N//i
        mn = min(mn,d+i-2)
print(mn)