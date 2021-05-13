import sys
from collections import Counter

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
A = LI()
counter_a = Counter(A)
choice_total = sum([(count*(count-1)//2) for count in counter_a.values() if count > 1])

for i in range(0, N):
    sub_num = A[i]
    count_sub_num = counter_a[sub_num]
    print(choice_total - ((count_sub_num*(count_sub_num-1) - (count_sub_num-1)*(count_sub_num-2)) // 2))