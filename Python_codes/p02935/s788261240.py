N = int(input())
V = sorted(list(map(int,input().split())))

ans = (V[0]+V[1])/2**(len(V)-1)

for i in range(2,N):
    ans += V[i]/2**(N-i)

print(ans)