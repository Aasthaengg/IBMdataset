N = int(input())
A,B=map(int,input().split())
P_s = list(map(int,input().split()))
CNT_s = [0]*3
for P in P_s:
    if P <= A:
        CNT_s[0] += 1
    elif A <  P <= B:
        CNT_s[1] += 1
    if B <  P:
        CNT_s[2] += 1
print(min(CNT_s))