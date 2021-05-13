def inN():
    return int(input())
def inL():
    return list(map(int,input().split()))
def inNL(n):
    return [list(map(int,input().split())) for i in range(n)]

n = inN()
N = n % 10
if n % 10 == 3:
    print("bon")
elif n%10 == 0 or n%10 == 1 or N == 6 or N == 8:
    print("pon")
else:
    print("hon")