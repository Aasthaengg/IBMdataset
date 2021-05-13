n = int(input())
#n, k = map(int, input().split())
al = list(map(int, input().split()))
#al=[list(input()) for i in range(n)]

print(max(al)-min(al))