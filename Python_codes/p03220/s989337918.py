N = int(input())
T,A = map(int,input().split())
B = [abs(A - (T-a*0.006)) for a in map(int,input().split())]
print(B.index(min(B))+1)