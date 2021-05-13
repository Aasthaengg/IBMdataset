N=int(input())
s=input()
t=input()
for x in range(N):
    for y in range(N-x):
        if s[x+y] != t[y]:
            break
    else:
        print(N+x)
        break
else:
    print(N*2)