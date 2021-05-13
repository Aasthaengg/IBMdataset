import sys

K = int(input())

if K % 2 == 0 or K % 5 == 0:
    print("-1")
    sys.exit()

x = 1
for i in range(1, 1000000):
    if (x * 7) % K == 0:
        print(i)
        sys.exit()
    x = (x + pow(10,i,K))%K

print("-1")
sys.exit()
