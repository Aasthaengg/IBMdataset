N = int(input())
print(sum(sorted(list(map(int,input().split())))[::-1][1:2*N:2]))