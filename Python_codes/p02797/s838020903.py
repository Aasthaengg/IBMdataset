from sys import stdin
#n = int(stdin.readline().rstrip())
#l = list(map(int, stdin.readline().rstrip().split()))
n,k,s = map(int, stdin.readline().rstrip().split())
#S = [list(map(int, stdin.readline().rstrip().split())) for _ in range(h)]#hの定義を忘れずに

for i in range(k):
    print(s, end=" ")

if s == 10**9:
    for i in range(n-k):
        if i == n-k-1:
            print(1)
            exit()
        else:
            print(1, end=" ")

else:
    for i in range(n-k):
        if i == n-k-1:
            print(s+1)
            exit()
        else:
            print(s+1, end=" ")
