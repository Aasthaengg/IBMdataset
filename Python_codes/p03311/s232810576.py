N = int(input())
A = list(map(int,input().split()))
Am = [a-i-1 for i,a in enumerate(A)]
Am.sort()
B = Am[N//2]
print(sum(abs(a-B) for a in Am))