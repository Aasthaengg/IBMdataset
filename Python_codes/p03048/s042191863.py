R,G,B,N = map(int, input().split())
answer = 0
for i in range(N+1):
    for j in range(N+1):
        if N>=(i*R+j*G) and  (N-(i*R+j*G))%B==0:
            answer += 1
print(answer)