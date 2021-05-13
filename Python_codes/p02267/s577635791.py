n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))
a = []*n

S_s =set(S)
T_s =set(T)
C = S_s & T_s
print(len(C))
