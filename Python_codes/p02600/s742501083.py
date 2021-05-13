import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = int(readline())
dic1 = {
    4:8,
    6:7,
    8:6,
    10:5,
    12:4,
    14:3,
    16:2,
    18:1,
}
for i in range(4,19,2):
    if i*100 <= n < (i+2)*100:
        print(dic1[i])