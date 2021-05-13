A,B=map(int,input().split())
print(sum(sorted([A,B,A-1,B-1])[-2:]))