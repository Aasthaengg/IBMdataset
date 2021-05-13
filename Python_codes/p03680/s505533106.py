N = int(input())

L = []
for i in range(N):
    L.append(int(input()))

State = [1]
for _ in range(N-1):
    State.append(0)

i=0
count=1
while 1:
    i = L[i]-1
    if State[i]==1:
        print(-1)
        exit()

    if i+1 == 2:
        print(count)
        exit()

    State[i]=1
    count+=1