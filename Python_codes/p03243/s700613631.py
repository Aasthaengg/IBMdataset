N = int(input())

for i in range(N,1000,1):
    n = list(str(i))
    if n[0]==n[1] and n[1]==n[2]:
        print(i)
        break