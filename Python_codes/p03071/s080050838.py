A,B=map(int,input().split())

C=[A+(A-1),A+B,B+(B-1)]

print(max(C))