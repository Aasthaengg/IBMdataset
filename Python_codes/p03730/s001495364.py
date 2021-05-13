A,B,C = map(int,input().split())
for i in range(A,A*B+1,A):
    if i%B==C:
        print("YES")
        break
else:
    print("NO")