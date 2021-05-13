W,a,b=map(int, input().split())
print(0 if W>=abs(b-a) else min(abs(b-a-W),abs(a-b-W)))