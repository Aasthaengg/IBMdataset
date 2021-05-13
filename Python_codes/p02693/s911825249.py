n = int(input())
low, high = map(int,input().split())
for i in range(low, high + 1):
    if i % n == 0:
        print("OK")
        exit()
        
print("NG")