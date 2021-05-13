N,M,C = map(int,input().split())
B_List =  list(map(int,input().split()))
Counter = 0
for i in range(N):
    Corrent_List = list(map(int,input().split()))
    Number = 0
    for j in range(M):
        Number += Corrent_List[j]*B_List[j]
    Number += C
    if Number > 0:
        Counter += 1

print(Counter)