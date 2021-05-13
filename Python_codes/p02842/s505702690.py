n=int(input())
import math
print( math.ceil(n/1.08) if math.floor(math.ceil(n/1.08)*1.08)==n else ":(")