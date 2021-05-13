N=int(input())
s=input()
t=input()
common=0

for start in range(N):
    point=0
    check=False
    for i in range(start,N):
        if s[i] != t[point]:
            check=True
            break
        point+=1
    if not check:
        common=N-start
        break

print(len(s)+len(t)-common)