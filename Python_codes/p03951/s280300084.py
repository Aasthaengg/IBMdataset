N=int(input())
s=input()
t=input()
for i in range(N+1):
    for j in range(N-i):
        if s[i+j]!=t[j]:
            break
    else:
        print(N+i)
        break