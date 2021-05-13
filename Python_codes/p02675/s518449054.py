import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

n = ini()
if n%10 == 3:
    print("bon")
elif n%10 in [0, 1, 6, 8]:
    print("pon")
else:
    print("hon")