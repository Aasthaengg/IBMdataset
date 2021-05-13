N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))

kion = [abs(T-0.006*H[i]-A) for i in range(N)]
print(kion.index(min(kion))+1)
