A,B,C = map(int,input().split())

ans = False
if C >=A and C <= B:
    ans = True
print("Yes" if ans else "No")