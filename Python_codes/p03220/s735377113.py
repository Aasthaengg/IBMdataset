N = int(input())
T,A = [int(i) for i in input().split()]
H = [abs(A-(T-int(i)*0.006)) for i in input().split()]

print(H.index(min(H))+1)
