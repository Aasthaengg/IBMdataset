N = int(input())

a = sorted(list(map(int,input().split())),reverse=True)

Alice = sum([a[i] for i in range(N) if i%2 == 0])
Bob= sum([a[i] for i in range(N) if i%2 == 1])
print(Alice-Bob)