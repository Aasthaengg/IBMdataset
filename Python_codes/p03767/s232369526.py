n=int(input())
print(sum(sorted(list(map(int,input().split())),reverse=True)[1:2*n:2]))