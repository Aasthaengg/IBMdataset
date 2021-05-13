#136-A

A,B,C = map(int,input().split())

#print(C - A + B)

ans = C - A + B

if ans <= 0:
    print(0)

else:
    print(ans)
