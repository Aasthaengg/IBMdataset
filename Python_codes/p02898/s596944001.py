import sys

def ILI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def ISI(): return map(int, sys.stdin.readline().rstrip().split())

n, k = ISI()
H = ILI()
cnt=0
for h in H:
	if h>=k:cnt+=1
print(cnt)