import io
import math

nim, mon = list(map(int, input().split()))
print((nim-1)//(mon*2+1)+1)