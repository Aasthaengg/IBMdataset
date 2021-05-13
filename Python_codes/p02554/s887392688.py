import math

N=int(input())
if N==1:
    result=0
else:
    # 全体-0含まない-9含まない+0も9も含まない
    result=(10**N-2*(9**N)+8**N)%(10**9+7)

print(result)