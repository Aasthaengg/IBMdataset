#累積xor
#累積和

N = int(input())
A = [0] + list(map(int,input().split()))

#累積xor
ruiseki_xor = [A[i] for i in range(N+1)]
for i in range(1,N+1,1):
    ruiseki_xor[i]=ruiseki_xor[i-1]^A[i]

#累積和
ruiseki = [0]*(N+1)
for i in range(1,N+1,1):
    ruiseki[i]=ruiseki[i-1]+A[i]

ans = 0
cersol = 1
for i in range(1,N+1,1):
    ans += cersol-i
    for j in range(cersol,N+1,1):
        if ruiseki[j]-ruiseki[i-1] == ruiseki_xor[j]^ruiseki_xor[i-1]:
            ans += 1
            cersol = j
        else:
            cersol = j
            break
        
        

print(ans)
