a,b = map(int, input().split())
import math
print(math.ceil((b-a)/(a-1)+1)) if b != 1 else print(0)