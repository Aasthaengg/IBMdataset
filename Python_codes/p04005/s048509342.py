A,B,C = map(int,input().split())
#if A%2 == 0 or B%2 == 0 or C%2 == 0 :
#    print(0)
#    exit()
L = abs(A*B*(C//2) - (A*B*(C-C//2)))
N = abs(A*C*(B//2) - (A*C*(B-B//2)))
M = abs(C*B*(A//2) - (C*B*(A-A//2)))

print(min(L,N,M))