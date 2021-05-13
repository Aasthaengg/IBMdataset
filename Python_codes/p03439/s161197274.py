import sys
readline = sys.stdin.readline
flush = sys.stdout.flush
def query(x):
    print("%d\n" % x)
    flush()
    # ジャッジから返される値を取得
    return readline().strip()


n = int(input())

right = n-1
left = 0

print(0, flush = True)
lefti = input()
if lefti == "Vacant":
    exit(0)
print(n-1, flush = True)
righti = input()
if righti == "Vacant":
    exit(0)

while True:
    mid = left + (right-left)//2
    midi = query(mid)
    if midi == "Vacant":
        exit(0)
    if (lefti == midi and (mid - left) % 2 == 1) or ((lefti != midi) and (mid - left) % 2 == 0):
        righti = midi
        right = mid
    else:
        lefti = midi
        left = mid
