from collections import Counter

N=int(input())
D=Counter((list(map(int,input().split()))))
M=int(input())
T=Counter((list(map(int,input().split()))))

for difficult,count in T.items():
    if difficult in D and D[difficult]>=count:
        pass
    else:
        print("NO")
        exit()
print("YES")