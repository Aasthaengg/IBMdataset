import math
N, X, T = map(int,input().split())
takoyakitime=math.ceil(N/X)
t_takoyakitime = takoyakitime*T
print(t_takoyakitime)