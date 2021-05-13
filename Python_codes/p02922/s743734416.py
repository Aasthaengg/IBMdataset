a,b = list(map(int,input().split()))

sasikomi = 1
tap = 0

while(sasikomi < b):
    tap = tap + 1
    sasikomi = sasikomi + a - 1

print(tap)
