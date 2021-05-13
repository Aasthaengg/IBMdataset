A,B,C = map(int,input().split())
for i in range(A,A*100000,A):
    if(i % B == C):
        print("YES")
        exit()
print("NO")