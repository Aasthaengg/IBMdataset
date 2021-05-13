import math
N = int(input())
judge_l = [pow(2,i) for i in range(0,10) if pow(2,i) <= N]
print(judge_l[-1])