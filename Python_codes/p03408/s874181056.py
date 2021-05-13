N=int(input())
s=[input() for i in range(N)]
M=int(input())
t=[input() for i in range(M)]
s2=list(set(s))
counter=0
for i in range(len(s2)):
    if s.count(s2[i])-t.count(s2[i])>counter:
        counter=s.count(s2[i])-t.count(s2[i])

print(counter)
