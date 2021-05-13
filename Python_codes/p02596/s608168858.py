#C
import sys
k=int(input())
s=0

for i in range(k):
    s=s*10+7
    if s%k!=0:
        s=s%k
    else:
        print(i+1)
        sys.exit()
print(-1)