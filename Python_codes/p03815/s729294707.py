import math
x=int(input())
div,mod=divmod(x,11)
alpha=math.ceil(mod/6)
print(div*2+alpha)